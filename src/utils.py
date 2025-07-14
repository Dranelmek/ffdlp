import os
import json
import subprocess

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
            "TEMPFILEPATH": "output/temp",
            "STATICOUTPUTNAME": "output",
            "USESTATICOUTPUTNAME": False
        }
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
    return config

def save_config(config, config_path="config.json"):
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

def edit_config(config, key, value, config_path="config.json"):
    config[key] = value
    save_config(config, config_path)

def run_command(command):
    subprocess.run(command, shell=True)

def get_temp_files(directory="output/temp"):
    if not os.path.exists(directory):
        return []
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]