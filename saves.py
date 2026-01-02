
import json, os
SAVE_DIR = "saves"

def save_game(slot, data):
    os.makedirs(SAVE_DIR, exist_ok=True)
    with open(f"{SAVE_DIR}/slot{slot}.json", "w") as f:
        json.dump(data, f)

def load_game(slot):
    try:
        with open(f"{SAVE_DIR}/slot{slot}.json", "r") as f:
            return json.load(f)
    except:
        return None
