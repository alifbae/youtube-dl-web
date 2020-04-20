# YOUTUBE-DL-WEB

Run `youtube-dl` as a web server allowing you to download youtube urls as mp3 files.

## Requirements

- Python -v 3.8.2
- dotenv
- ffmpeg

## Installing

- `pip install -r requirements`

## Usage

- set the following environment variables in your shell or a `.env` file
  - FLASK_APP=[runserver]
  - FLASK_ENV=[development/production]
  - SECRET=[your-secret-key]
- `flask run` or `python -m runserver.py`
  - will start a flask server at `0.0.0.0:5000`

## Todo

- [] Error Logging
- [] Sqlite db
- [] AJAX requests
