"""Download Shibuya live streaming
Caution: need to kill ps(&ffmpeg ps) after execute
"""
import pafy
import youtube_dl
import time

SHIBUYA = "lkIJYc4UH60"
URL = "https://www.youtube.com/watch?v=" + SHIBUYA

p = pafy.new(URL)
b = p.streams[1]
url = p.streams[1].url

ydl_opts = {
    "outtmpl": "statics/cap.mp4",
    "nopart": True,
    "quiet": True,
}

def download(url: str):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    download(url)
