# FFDLP
FFDLP is a simple GUI that for downloading videos using yt-dlp and converting/compressing video files with ffmpeg.

## Installation

The executables are currently not hosted for download. to obtain them download one of the two zip files (with or without ytdlp & ffmpeg included) in the "executables" folder and unpack them, or clone the repository and run:

```bash
pip install pyinstaller
pyinstaller --onefile --icon=logo.ico ffdlp.py
```
from the root of the project.

## Usage

To use either run ffdlp.exe directly or open the folder containing the executable in command prompt and run:
```bash
ffdlp
```
Ensure that both executables for yt-dlp and ffmpeg are up to date and in the same folder as the executable. This program is just a QOL GUI and will not function without those two. Full credit for [yt-dlp](https://github.com/yt-dlp/yt-dlp) goes to the yt-dlp devs and contributors. Full credit for [ffmpeg](https://ffmpeg.org/) goes to the ffmpeg devs and contributors.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
also check out my website at:
[https://bit-by-bit-st.web.app/](https://bit-by-bit-st.web.app/)

Please make sure to add/update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)