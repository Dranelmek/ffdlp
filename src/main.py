# This is a program that uses yt-dlp to download YouTube videos.
# It can use ffmpeg to convert the downloaded videos if needed.
# It also saves the user's preferences in a configuration file.
# Note: Ensure that yt-dlp is installed and available in your PATH.
# Note: Also ensure that yt-dlp ffmpeg's executables are in the project folder.

import subprocess
from utils import *
from dlp import *

def run_command(command):
    subprocess.run(command, shell=True)

def main():
    config = load_or_create_config()
    if config["AUTONAMEGEN"]:
        run_command(auto_ytdlp(config["test_url"]))
    else:
        run_command(std_ytdlp(config["test_url"]))
    

if __name__ == "__main__":
    main()

# TODO build GUI and add the other scripts