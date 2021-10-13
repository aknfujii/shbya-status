"""Download Shibuya live streaming
Caution: need to kill ps(&ffmpeg ps) after execute
"""
import pafy
import youtube_dl
import time

from config import FILEPATH

SHIBUYA = "HpdO5Kq3o7Y"
URL = "https://www.youtube.com/watch?v=" + SHIBUYA

p = pafy.new(URL)
b = p.streams[1]
url = p.streams[1].url

ydl_opts = {
    "outtmpl": FILEPATH,
    "nopart": True,
    "quiet": True,
    'Video':'libx264',
    'Audio':'wav',
    'AV':'mkv',
}

def download(url: str):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    download(url)
