from flask import Flask, request, redirect, url_for, render_template
from youtube_dl import YoutubeDL
from helpers import sanitize_input

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        text = request.form['url-text']

        print(text)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )