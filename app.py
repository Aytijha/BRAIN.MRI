import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

ASSET_FOLDER = 'static/assets/'

app = Flask(__name__)
app.config['ASSET_FOLDER'] = ASSET_FOLDER

github_icon = os.path.join(app.config['ASSET_FOLDER'], 'icons8-github-50.png')
instagram_icon = os.path.join(app.config['ASSET_FOLDER'], 'instagram.png')
twitter_icon = os.path.join(app.config['ASSET_FOLDER'], 'twitter.png')
bg_video = os.path.join(app.config['ASSET_FOLDER'], 'pexels-tima-miroshnichenko-6010766.mp4')
    
@app.route('/')
def upload_form():
    return render_template('index.html', type="", githubicon=github_icon, instagramicon=instagram_icon, twittericon=twitter_icon, bgvideo=bg_video)

@app.route('/', methods=['POST'])
def upload_image():
    print('post')
    c = 'xyz'
    return render_template('index.html', type="Patient is suffering from "+c+" type Alzheimers", githubicon=github_icon, instagramicon=instagram_icon, twittericon=twitter_icon, bgvideo=bg_video)

if __name__ == "__main__":
    app.run(debug=True)