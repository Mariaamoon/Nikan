"""
Quote dataset — each quote has:
  - text:   the quote itself
  - author: who said it
  - topics: list of topic tags
  - mood:   emotional tone
  - length: 'short' | 'medium' | 'long'
"""

QUOTES =[
    {
        "text": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
        "topics": ["work", "passion", "success"],
        "mood": "motivational",
        "length": "short",
    },
    {
        "text": "In the middle of every difficulty lies opportunity.",
        "author": "Albert Einstein",
        "topics": ["difficulty", "opportunity", "resilience"],
        "mood": "motivational",
        "length": "short",
    },
    {
        "text": "Imagination is more important than knowledge.",
        "author": "Albert Einstein",
        "topics": ["imagination", "creativity", "knowledge"],
        "mood": "inspirational",
        "length": "short",
    },
    {
        "text": "Life is what happens when you're busy making other plans.",
        "author": "John Lennon",
        "topics": ["life", "plans", "mindfulness"],
        "mood": "reflective",
        "length": "short",
    },
    {
        "text": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt",
        "topics": ["future", "dreams", "belief"],
        "mood": "motivational",
        "length": "medium",
    },
    {
        "text": "It is during our darkest moments that we must focus to see the light.",
        "author": "Aristotle",
        "topics": ["darkness", "hope", "resilience", "focus"],
        "mood": "hopeful",
        "length": "medium",
    },
    {
        "text": "Spread love everywhere you go. Let no one ever come to you without leaving happier.",
        "author": "Mother Teresa",
        "topics": ["love", "kindness", "happiness"],
        "mood": "uplifting",
        "length": "medium",
    },
    {
        "text": "When you reach the end of your rope, tie a knot in it and hang on.",
        "author": "Franklin D. Roosevelt",
        "topics": ["perseverance", "strength", "resilience"],
        "mood": "motivational",
        "length": "medium",
    },
    {
        "text": "Always remember that you are absolutely unique. Just like everyone else.",
        "author": "Margaret Mead",
        "topics": ["uniqueness", "identity", "humor"],
        "mood": "humorous",
        "length": "short",
    },
    {
        "text": "Do not go where the path may lead, go instead where there is no path and leave a trail.",
        "author": "Ralph Waldo Emerson",
        "topics": ["leadership", "courage", "independence"],
        "mood": "inspirational",
        "length": "medium",
    },
    {
        "text": "You will face many defeats in life, but never let yourself be defeated.",
        "author": "Maya Angelou",
        "topics": ["defeat", "resilience", "strength"],
        "mood": "motivational",
        "length": "medium",
    },
    {
        "text": "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "author": "Nelson Mandela",
        "topics": ["resilience", "glory", "perseverance"],
        "mood": "inspirational",
        "length": "long",
    },
    {
        "text": "In the end, it's not the years in your life that count. It's the life in your years.",
        "author": "Abraham Lincoln",
        "topics": ["life", "meaning", "time"],
        "mood": "reflective",
        "length": "medium",
    },
    {
        "text": "Never let the fear of striking out keep you from playing the game.",
        "author": "Babe Ruth",
        "topics": ["fear", "courage", "action"],
        "mood": "motivational",
        "length": "short",
    },
    {
        "text": "Life is either a daring adventure or nothing at all.",
        "author": "Helen Keller",
        "topics": ["life", "adventure", "courage"],
        "mood": "inspirational",
        "length": "short",
    },
    {
        "text": "Many of life's failures are people who did not realize how close they were to success when they gave up.",
        "author": "Thomas Edison",
        "topics": ["failure", "success", "perseverance"],
        "mood": "motivational",
        "length": "long",
    },
    {
        "text": "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose.",
        "author": "Dr. Seuss",
        "topics": ["choices", "independence", "potential"],
        "mood": "uplifting",
        "length": "long",
    },
    {
        "text": "If life were predictable it would cease to be life, and be without flavor.",
        "author": "Eleanor Roosevelt",
        "topics": ["life", "unpredictability", "adventure"],
        "mood": "reflective",
        "length": "short",
    },
    {
        "text": "If you look at what you have in life, you'll always have more.",
        "author": "Oprah Winfrey",
        "topics": ["gratitude", "abundance", "mindfulness"],
        "mood": "uplifting",
        "length": "short",
    },
    {
        "text": "Two roads diverged in a wood, and I took the one less traveled by, and that has made all the difference.",
        "author": "Robert Frost",
        "topics": ["choices", "individuality", "courage"],
        "mood": "reflective",
        "length": "long",
    },
    {
        "text": "It does not matter how slowly you go as long as you do not stop.",
        "author": "Confucius",
        "topics": ["perseverance", "progress", "patience"],
        "mood": "motivational",
        "length": "short",
    },
    {
        "text": "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.",
        "author": "Thomas Edison",
        "topics": ["weakness", "success", "persistence"],
        "mood": "motivational",
        "length": "long",
    },
    {
        "text": "You miss 100% of the shots you don't take.",
        "author": "Wayne Gretzky",
        "topics": ["action", "opportunity", "courage"],
        "mood": "motivational",
        "length": "short",
    },
    {
        "text": "Whether you think you can or you think you can't, you're right.",
        "author": "Henry Ford",
        "topics": ["mindset", "belief", "success"],
        "mood": "motivational",
        "length": "short",
    },
    {
        "text": "I have learned over the years that when one's mind is made up, this diminishes fear.",
        "author": "Rosa Parks",
        "topics": ["courage", "fear", "determination"],
        "mood": "inspirational",
        "length": "medium",
    },
    {
        "text": "I alone cannot change the world, but I can cast a stone across the waters to create many ripples.",
        "author": "Mother Teresa",
        "topics": ["change", "impact", "hope"],
        "mood": "hopeful",
        "length": "medium",
    },
    {
        "text": "No act of kindness, no matter how small, is ever wasted.",
        "author": "Aesop",
        "topics": ["kindness", "generosity", "impact"],
        "mood": "uplifting",
        "length": "short",
    },
    {
        "text": "We know what we are, but know not what we may be.",
        "author": "William Shakespeare",
        "topics": ["potential", "identity", "philosophy"],
        "mood": "reflective",
        "length": "short",
    },
    {
        "text": "Good friends, good books, and a sleepy conscience: this is the ideal life.",
        "author": "Mark Twain",
        "topics": ["friendship", "books", "happiness", "humor"],
        "mood": "humorous",
        "length": "short",
    },
    {
        "text": "Happiness is not something ready made. It comes from your own actions.",
        "author": "Dalai Lama",
        "topics": ["happiness", "action", "mindfulness"],
        "mood": "uplifting",
        "length": "short",
    },
]

# All unique values — useful for building intent classifiers
ALL_MOODS   = sorted({q["mood"]   for q in QUOTES})
ALL_TOPICS  = sorted({t           for q in QUOTES for t in q["topics"]})
ALL_AUTHORS = sorted({q["author"] for q in QUOTES})

if __name__ == "__main__":
    print(f"Total quotes : {len(QUOTES)}")
    print(f"Moods        : {ALL_MOODS}")
    print(f"Unique topics: {len(ALL_TOPICS)}")
    print(f"Authors      : {len(ALL_AUTHORS)}")
