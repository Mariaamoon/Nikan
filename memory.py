import json
import os

MEMORY_FILE = "user_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    return {"name": None}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

memory = {
    "name": None
}

def set_name(name):
    memory["name"] = name
    save_memory(memory)

def get_name():
    return memory["name"]

import re

def extract_name(text):
    match = re.search(r"(?:my name is|i am|i'm)\s+([A-Za-z]+)", text, re.IGNORECASE)

    if match:
        return match.group(1)

    return None