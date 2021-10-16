import os
import random
from flask import (
        Flask, 
        send_from_directory,
        render_template,
        url_for,
        )

app = Flask('mk3supra', static_url_path='', static_folder='static', template_folder='templates')

@app.route("/")
def hello_world():
        return render_template('index.html')

@app.route("/external-docs")
def external_docs():
        return render_template('external-docs.html')

@app.route("/external-parts")
def external_parts():
        return render_template('external-parts.html')

@app.route("/brochure-art")
def art_ep():
        art_folder = 'img/brochure'
        filenames = os.listdir(os.path.join(app.static_folder, art_folder))
        paths = [url_for('static', filename=os.path.join(art_folder, f)) for f in filenames]
        random.shuffle(paths)
        return render_template('brochure-art.html', art=paths)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
