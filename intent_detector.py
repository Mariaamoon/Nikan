"""
Intent Detector
===============
Classifies a user message into one of four intents:

  MOOD_REQUEST   — "give me something motivational"
  TOPIC_REQUEST  — "a quote about friendship"
  AUTHOR_REQUEST — "quote by Einstein"
  RANDOM         — "surprise me" / anything else

Then extracts entities (mood, topics, author) from the message
using keyword matching + spaCy NER for author names.

Usage:
    from nlp.intent_detector import IntentDetector
    detector = IntentDetector()
    result = detector.detect("give me a quote by Einstein about curiosity")
    # → {"intent": "AUTHOR_REQUEST", "author": "Albert Einstein",
    #    "topics": ["curiosity"], "mood": None, "raw": "..."}
"""

import re
import spacy
from quotes import ALL_MOODS, ALL_TOPICS, ALL_AUTHORS, QUOTES

# ---------------------------------------------------------------------------
# Keyword maps — expand these as your dataset grows
# ---------------------------------------------------------------------------

MOOD_KEYWORDS = {
    "motivational":  ["motivat", "motivate", "pump", "inspire me", "push me",
                      "drive", "fire me up", "get going", "keep going"],
    "inspirational": ["inspir", "uplift", "spark", "ignit", "awaken"],
    "reflective":    ["reflect", "think", "ponder", "contemplate", "deep",
                      "philosophical", "meaning", "life"],
    "hopeful":       ["hope", "hopeful", "optimis", "bright side", "light",
                      "better days"],
    "humorous":      ["funny", "humor", "humour", "laugh", "joke", "witty",
                      "amusing", "lightheart"],
    "uplifting":     ["uplift", "cheer", "happy", "happiness", "joy",
                      "positive", "smile", "feel good"],
}

AUTHOR_TRIGGER_WORDS = [
    "by", "from", "said by", "quote by", "words by", "according to"
]

TOPIC_TRIGGER_WORDS = [
    "about", "on", "regarding", "related to", "concerning", "on the topic of"
]

RANDOM_TRIGGERS = [
    "random", "surprise", "anything", "whatever", "just a quote",
    "any quote", "give me one", "pick one"
]


# ---------------------------------------------------------------------------
# Author name aliases — map partial names → canonical dataset names
# ---------------------------------------------------------------------------

AUTHOR_ALIASES: dict[str, str] = {}
for _author in ALL_AUTHORS:
    parts = _author.lower().split()
    for part in parts:
        if len(part) > 3:                     # skip "Dr.", "Jr." etc.
            AUTHOR_ALIASES[part] = _author
    AUTHOR_ALIASES[_author.lower()] = _author  # full name match


class IntentDetector:
    """Detect intent and extract entities from a raw user message."""

    def __init__(self):
        # Load the small English spaCy model for NER (person detection)
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            raise RuntimeError(
                "spaCy model not found. Run:\n"
                "  python -m spacy download en_core_web_sm"
            )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def detect(self, user_message: str) -> dict:
        """
        Returns a dict:
          intent  : 'MOOD_REQUEST' | 'TOPIC_REQUEST' |
                    'AUTHOR_REQUEST' | 'RANDOM'
          mood    : str | None
          topics  : list[str]
          author  : str | None   (canonical name from dataset)
          raw     : original message
        """
        msg   = user_message.strip()
        lower = msg.lower()

        mood   = self._extract_mood(lower)
        topics = self._extract_topics(lower)
        author = self._extract_author(lower, msg)

        intent = self._classify_intent(lower, mood, topics, author)

        return {
            "intent": intent,
            "mood":   mood,
            "topics": topics,
            "author": author,
            "raw":    msg,
        }

    # ------------------------------------------------------------------
    # Intent classification
    # ------------------------------------------------------------------

    def _classify_intent(
        self,
        lower: str,
        mood: str | None,
        topics: list[str],
        author: str | None,
    ) -> str:
        # Random / catch-all triggers first
        if any(t in lower for t in RANDOM_TRIGGERS):
            return "RANDOM"

        # Explicit priority: author > topic > mood > random
        if author:
            return "AUTHOR_REQUEST"
        if topics:
            return "TOPIC_REQUEST"
        if mood:
            return "MOOD_REQUEST"

        # Fallback — treat as a semantic search (handled by Step 5)
        return "SEMANTIC_SEARCH"

    # ------------------------------------------------------------------
    # Entity extractors
    # ------------------------------------------------------------------

    def _extract_mood(self, lower: str) -> str | None:
        """Return the first matching mood keyword category, or None."""
        for mood, keywords in MOOD_KEYWORDS.items():
            if any(kw in lower for kw in keywords):
                return mood
        return None

    def _extract_topics(self, lower: str) -> list[str]:
        """
        Find topic trigger words, then look for dataset topic tags
        in the words that follow them.
        Also does a broad scan of all topic words directly in the message.
        """
        matched = set()

        # 1. Scan for any dataset topic directly in message
        for topic in ALL_TOPICS:
            # Use word boundaries so "hope" doesn't match "hopeful"
            if re.search(rf"\b{re.escape(topic)}\b", lower):
                matched.add(topic)

        # 2. Look for explicit "about X" constructions and extract the noun
        for trigger in TOPIC_TRIGGER_WORDS:
            idx = lower.find(trigger)
            if idx != -1:
                after = lower[idx + len(trigger):].strip()
                first_word = after.split()[0] if after.split() else ""
                for topic in ALL_TOPICS:
                    if first_word.startswith(topic[:4]):
                        matched.add(topic)

        return sorted(matched)

    def _extract_author(self, lower: str, original: str) -> str | None:
        """
        Two-pass author detection:
          1. spaCy NER — finds PERSON entities in the original cased text
          2. Keyword alias fallback — checks AUTHOR_ALIASES dict
        """
        # Pass 1: spaCy NER
        doc = self.nlp(original)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                candidate = ent.text.lower()
                # Try to match against known authors
                if candidate in AUTHOR_ALIASES:
                    return AUTHOR_ALIASES[candidate]
                # Partial match (last name only, e.g. "Einstein")
                for alias, canonical in AUTHOR_ALIASES.items():
                    if candidate in alias or alias in candidate:
                        return canonical

        # Pass 2: Keyword alias scan (catches names spaCy misses)
        for alias, canonical in AUTHOR_ALIASES.items():
            if re.search(rf"\b{re.escape(alias)}\b", lower):
                return canonical

        return None


# ---------------------------------------------------------------------------
# Quick smoke-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    detector = IntentDetector()

    test_messages = [
        "Give me a motivational quote",
        "I need something about friendship and kindness",
        "Quote by Einstein",
        "Give me a quote by Maya Angelou about resilience",
        "Surprise me!",
        "Something deep and reflective please",
        "I want a funny quote",
        "Tell me what Steve Jobs said",
    ]

    print("=" * 60)
    for msg in test_messages:
        result = detector.detect(msg)
        print(f"\nInput  : {msg}")
        print(f"Intent : {result['intent']}")
        print(f"Mood   : {result['mood']}")
        print(f"Topics : {result['topics']}")
        print(f"Author : {result['author']}")
    print("=" * 60)
