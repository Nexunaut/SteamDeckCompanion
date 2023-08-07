import os
import json

config_file = os.path.expanduser("~/.config/SteamDeckCompanion/configuration")

def save_settings(data):
    os.makedirs(os.path.dirname(config_file), exist_ok=True)
    
    with open(config_file, "w") as file:
        json.dump({"theme": data}, file)
        
def load_settings():
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            return json.load(file)
    else:
        return {"theme": "light"}