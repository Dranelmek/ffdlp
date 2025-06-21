import subprocess

def std_ytdlp(url):
    # This function returns the yt-dlp command to search for a YouTube video
    # and download it using the provided URL.
    # The URL is hardcoded in this example.
    # Note: Ensure that yt-dlp is installed and available in your PATH.
    return f'yt-dlp "ytsearch:{url}"'

subprocess.run(std_ytdlp("https://www.youtube.com/watch?v=QjMpPozJLpA"), shell=True)

# TODO build GUI and add the other scripts