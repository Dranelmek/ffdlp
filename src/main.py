# This is a program that uses yt-dlp to download YouTube videos.
# It can use ffmpeg to convert the downloaded videos if needed.
# It also saves the user's preferences in a configuration file.
# Note: Ensure that yt-dlp is installed and available in your PATH.
# Note: Also ensure that yt-dlp ffmpeg's executables are in the project folder.

import subprocess
from utils import *
from scripts import *
from os import listdir
from os.path import isfile, join

def test(conf):
    # if conf["AUTONAMEGEN"]:
    #     run_command(auto_ytdlp(conf["test_url"]))
    # elif conf["USESTATICOUTPUTNAME"]:
    #     run_command(auto_ytdlp(conf["test_url"], conf["STATICOUTPUTNAME"]))
    # else:
    #     run_command(std_ytdlp(conf["test_url"]))
    # run_command(audio_ytdlp(conf["test_url"]))
    mypath = "output/temp"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print(f"Files in output/temp: {onlyfiles}")

def main():
    config = load_or_create_config()
    test(config)
    

if __name__ == "__main__":
    main()

# TODO build GUI and add the other scripts