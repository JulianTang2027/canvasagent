import json
import os

def load_state(path):
    
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_state(path, state):

    os.makedirs(os.path.dirname(path), exist_ok=True)

    try:
        with open(path, 'w') as file:
            json.dump(state, file)
    except:
        return

