# Version: 1.0.1
# Author: Kem (Drane)

# This is a program that uses yt-dlp to download YouTube videos.
# It can use ffmpeg to convert the downloaded videos if needed.
# It also saves the user's preferences in a configuration file.
# Note: Ensure that yt-dlp is installed and available in your PATH.
# Note: Also ensure that yt-dlp ffmpeg's executables are in the project folder.

from src.utils import *
from src.scripts import *
from src.gui import App

def main():
    intro = """
    Welcome to:

    ███████╗███████╗██████╗ ██╗     ██████╗
    ██╔════╝██╔════╝██╔══██╗██║     ██╔══██╗
    █████╗  █████╗  ██║  ██║██║     ██████╔╝
    ██╔══╝  ██╔══╝  ██║  ██║██║     ██╔═══╝
    ██║     ██║     ██████╔╝███████╗██║
    ╚═╝     ╚═╝     ╚═════╝ ╚══════╝╚═╝

    A simple GUI for yt-dlp and ffmpeg.
    Author: Kem (Drane)
    Version: 1.0.1
    This program is free software: you can redistribute it and/or modify
    GitHub: https://github.com/Dranelmek/ffdlp
    """
    if check_directory():
        try:
            print(intro)
        except UnicodeEncodeError:
            print("Welcome to FFDLP!\nA simple GUI for yt-dlp and ffmpeg.\nAuthor: Kem (Drane)\nThis program is free software: you can redistribute it and/or modify\nGitHub: https://github.com/Dranelmek/ffdlp")
        app = App()
        app.mainloop()
    else:
        print("Required executables are missing. Please ensure BOTH yt-dlp.exe and ffmpeg.exe are in the same folder as this application.\nExiting FFDLP...")


if __name__ == "__main__":
    main()