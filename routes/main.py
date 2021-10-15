from flask import (
        Flask, 
        send_from_directory,
        render_template,
        )

app = Flask('mk3supra', static_url_path='', static_folder='static', template_folder='templates')

@app.route("/")
def hello_world():
        return render_template('index.html')

@app.route("/another")
def rello_world():
        return "<p>Hello, Sorld!</p>"
