"""
This module serves as a wrapper to the youtube_dl library, containing methods to extract 
and download youtube urls and save as an mp3 file to disk
"""
from __future__ import unicode_literals
from youtube_dl import YoutubeDL

YTDL_OPTS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

def download_yt(url):
    with YoutubeDL(YTDL_OPTS) as ytdl:
        ytdl.download([url])