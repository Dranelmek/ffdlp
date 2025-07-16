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
            "DEFAULTOPTION": 0,
            "DEFAULTOUTPUTPATH": "output",
            "TEMPFILEPATH": "output/temp",
            "STATICOUTPUTNAME": "output",
            "USESTATICOUTPUTNAME": False
        }
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
    return config

def save_config(config, config_path="config.json"):
    config = {k: v for k, v in config.items() if v is not None}
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

def edit_config(config, key, value, config_path="config.json"):
    config[key] = value
    save_config(config, config_path)

def check_config(key, default=None):
    conf = load_or_create_config()
    if key not in conf:
        conf[key] = default
        save_config(conf)
    return conf[key]

def run_command(command):
    subprocess.run(command, shell=True)

def get_file_names(directory=check_config("TEMPFILEPATH")):
    if not os.path.exists(directory):
        return []
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def filename_without_extension(file_path):
        # get the file name from a path such as "output/temp/video.mp4" or "output\temp\video.mp4"
        return os.path.splitext(os.path.basename(file_path))[0]

def delete_temp_files(directory=check_config("TEMPFILEPATH")):
    if not os.path.exists(directory):
        return
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted temporary file: {file_path.encode("utf-8")}")