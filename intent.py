import re

def detect_intent(text):
    text = text.lower().strip()

    if re.search(r"\b(my name is|i am|i'm)\b", text):
        return "introduce"

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    if any(word in text for word in ["thanks", "thank you"]):
        return "thanks"

    if any(word in text for word in ["bye", "goodbye", "see you"]):
        return "goodbye"

    return "emotion"

print(detect_intent("Hi"))
# greeting

print(detect_intent("My name is Jam"))
# introduce

print(detect_intent("Thank you"))
# thanks

print(detect_intent("I feel lonely"))
# emotion