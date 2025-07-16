import datetime
import os
from utils import check_config, filename_without_extension

def auto_ytdlp(url, name=None):
    # This function returns the yt-dlp command to download a YouTube video
    # using the provided URL. If no name is provided, it uses the current date-time
    
    if name is None:
        name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    return f'yt-dlp -o "{check_config("TEMPFILEPATH")}/{name}.%(ext)s" "ytsearch:{url}"'

def std_ytdlp(url):
    # This function returns the yt-dlp command to download a YouTube video
    return f'yt-dlp -o "{check_config("TEMPFILEPATH")}/%(title)s.%(ext)s" "{url}"'

def audio_ytdlp(url):
    # This function returns the yt-dlp command to download a YouTube video as audio
    return f'yt-dlp -x --audio-format mp3 -o "{check_config("TEMPFILEPATH")}/%(title)s.%(ext)s" "{url}"'

def video_convert_mp4(input_file):
    # This function returns the ffmpeg command to convert a video file to mp4 format
    output_file = filename_without_extension(input_file)
    print(f"FILENAME WITHOUT EXTENSION: {output_file.encode('utf-8')}")
    return f'ffmpeg -i "{input_file}" -map 0 -c:v libx264 -preset slow -crf 23 -c:a aac -b:a 192k -movflags +faststart "{check_config("DEFAULTOUTPUTPATH")}/{output_file}.mp4"'