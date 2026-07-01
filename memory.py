memory = {
    "name": None
}

def set_name(name):
    memory["name"] = name


def get_name():
    return memory["name"]

import re

def extract_name(text):
    match = re.search(r"(?:my name is|i am|i'm)\s+([A-Za-z]+)", text, re.IGNORECASE)

    if match:
        return match.group(1)

    return None