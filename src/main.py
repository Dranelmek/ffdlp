# Version: 1.0.0
# Author: Kem (Drane)

# This is a program that uses yt-dlp to download YouTube videos.
# It can use ffmpeg to convert the downloaded videos if needed.
# It also saves the user's preferences in a configuration file.
# Note: Ensure that yt-dlp is installed and available in your PATH.
# Note: Also ensure that yt-dlp ffmpeg's executables are in the project folder.

from utils import *
from scripts import *
from gui import App


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()

# TODO: bundle into an executable