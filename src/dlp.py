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


