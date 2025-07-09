import os
import json

def load_or_create_config(config_path="config.json"):
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            try:
                config = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                config = {}
    else:
        config = {
            "AUTONAMEGEN": True,
            "DEFAULTOUTPUTPATH": "E:/Production/Magic/video",
            "test_name": "Waluigi lol",
            "test_url": "https://www.youtube.com/watch?v=ouq9rVFJNDk"
        }
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
    return config

def save_config(config, config_path="config.json"):
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)