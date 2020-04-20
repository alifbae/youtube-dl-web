"""
This file runs a flask web server as a web interface for youtube-dl
"""
from __future__ import unicode_literals
from os import getenv, listdir, path
from os.path import isfile, join
from urllib.parse import urlparse

from dotenv import load_dotenv
from flask import Flask, request, redirect, url_for, render_template, flash, send_from_directory
from youtube_dl import YoutubeDL
from youtube_dl.utils import DownloadError

# region: init
app = Flask(__name__)
load_dotenv()
app.secret_key = getenv('SECRET')
# endregion

# region: routes
@app.route('/', methods=['GET'])
def index():
    """
    return the index page
    """
    downloads = list_downloads(app.root_path)
    return render_template('index.html', downloads=downloads)

@app.route('/download', methods=['POST'])
def download():
    """
    process and download the incoming url
    """
    if request.method == 'POST':
        raw_url = request.form['url-text'].replace(' ', '')
        if urlparse(raw_url).hostname != "www.youtube.com":
            flash('Only URLs from Youtube allowed (for now)')
            return redirect(url_for('index'))

        download_yt(raw_url)
        return redirect(url_for('index'))

@app.route('/download_file/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory('./downloads', filename, as_attachment=True)
# endregion

# region: utils
def list_downloads(root_path):
    """
    returns a list of (file_path, file_name) from the downloads/ dir
    """
    downloads_path = path.join(root_path, 'downloads/')
    file_list = []
    for file_name in listdir(downloads_path):
      file_path = join(downloads_path, file_name)
      if isfile(file_path):
        file_list.append((file_name, file_path))
    return file_list

def download_yt(url):
    """
    download the url passed in args using the ytdl_options as options
    """
    ytdl_options = {
        'format': 'bestaudio/best',
        'outtmpl': './downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    max_retries = 4
    for i in range(max_retries):
        try:
            with YoutubeDL(ytdl_options) as ytdl:
                ytdl.download([url])
        except DownloadError:
            if i < max_retries -1:
                print("retrying")
                continue
        break
# endregion

# region: main
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# endregion
