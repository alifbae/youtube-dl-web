"""
This module runs a flask web server as a web interface for youtube-dl
"""

from os import getenv
from urllib.parse import urlparse
from flask import Flask, request, redirect, url_for, render_template, flash
from dotenv import load_dotenv
from ytdl_wrapper import download_yt

load_dotenv()
app = Flask(__name__)
app.secret_key = getenv('SECRET')

@app.route('/', methods=['GET'])
def index():
    """
    return the index page
    """
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    """
    process and download the incoming url
    """
    if request.method == 'POST':
        raw_url = request.form['url-text']
        parsed_url = urlparse(raw_url)
        if parsed_url.hostname != "www.youtube.com":
            flash('Only URLs from Youtube allowed (for now)')
            return redirect(url_for('index'))

        download_yt(parsed_url)
        return redirect(url_for('index'))

# https://www.youtube.com/watch?v=glaG64Ao7sM