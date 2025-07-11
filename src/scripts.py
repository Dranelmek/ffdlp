import datetime

def auto_ytdlp(url, name=None):
    # This function returns the yt-dlp command to download a YouTube video
    # using the provided URL. If no name is provided, it uses the current date-time
    
    if name is None:
        name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    return f'yt-dlp -o "output/temp/{name}.%(ext)s" "ytsearch:{url}"'

def std_ytdlp(url):
    # This function returns the yt-dlp command to download a YouTube video
    return f'yt-dlp -o "output/temp/%(title)s.%(ext)s" "{url}"'

def audio_ytdlp(url):
    # This function returns the yt-dlp command to download a YouTube video as audio
    return f'yt-dlp -x --audio-format mp3 -o "output/temp/%(title)s.%(ext)s" "{url}"'

def video_convert_mp4(input_file):
    # This function returns the ffmpeg command to convert a video file to mp4 format
    def filename_without_extension(file_path):
        return file_path.rsplit('.', 1)[0] if '.' in file_path else file_path
    output_file = filename_without_extension(input_file)
    return f'ffmpeg -i "{input_file}" -map 0 -c:v libx264 -preset slow -crf 23 -c:a aac -b:a 192k -movflags +faststart "{output_file}.mp4"'