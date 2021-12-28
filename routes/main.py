import os
import random
import markdown
import subprocess
from flask import (
    Flask, 
    jsonify,
    url_for,
    request,
    make_response,
    render_template,
    send_from_directory,
    redirect,
)
from markdown.extensions import tables
import flask_login
from logging.config import dictConfig
from werkzeug.utils import secure_filename
from .user import User

users = {'zubir@zubir.dev': {'password': 'secret'}}
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask('mk3supra', static_url_path='', static_folder='static', template_folder='templates')
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.jpeg', '.md', '.pdf']
app.config['UPLOAD_PATH'] = app.static_folder + '/uploads'

with open('routes/auth_key.secret', 'r') as fh:
    key = fh.read()
    app.secret_key = key

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

def fortune():
    return subprocess.run(['/usr/games/fortune'], stdout=subprocess.PIPE).stdout.decode('utf-8')

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user

@app.route("/")
def hello_world():
        return render_template('public/html/index.html', fortune=fortune())

@app.route("/external-docs")
def external_docs():
        return render_template('public/html/external-docs.html', fortune=fortune())

@app.route("/external-parts")
def external_parts():
        return render_template('public/html/external-parts.html', fortune=fortune())

@app.route("/brochure-art")
def art_ep():
        art_folder = 'img/brochure'
        filenames = os.listdir(os.path.join(app.static_folder, art_folder))
        paths = [url_for('static', filename=os.path.join(art_folder, f)) for f in filenames]
        random.shuffle(paths)
        return render_template('public/html/brochure-art.html', art=paths, fortune=fortune())

@app.route("/turboninjas")
def turboninjas():
        return render_template('public/html/turboninjas.html')

@app.route("/mk3supra/<path:subpath>")
def serve_turboninjas_files(subpath):
        return send_from_directory(app.static_folder, os.path.join('turboninjas', subpath))

@app.route("/writeups")
def writeups_index():
        return render_template('public/html/writeups-index.html', fortune=fortune())

@app.route("/tuning")
def tuning():
    markdown_file = 'tuning.md'
    path = os.path.join('templates/public/markdown', markdown_file)
    if os.path.exists(path):
        md = render_template('public/markdown/' + markdown_file)
        html = markdown.markdown(md, extensions=['tables'])
        return render_template("public/html/tuning.html", markdown=html, fortune=fortune())
    return render_template('public/html/404.html', fortune=fortune()), 404

@app.route("/writeups/<path:subpath>")
def writeups_page(subpath):
    path = os.path.join('templates/public/markdown', subpath + '.md')
    if os.path.exists(path):
        md = render_template('public/markdown/' + subpath + '.md')
        html = markdown.markdown(md)
        return render_template("public/html/writeup-template.html", title=subpath, content=html, fortune=fortune())
    return render_template('public/html/404.html', fortune=fortune()), 404

@app.route("/upload-img", methods=["GET", "POST"])
def img_upload():
    app.logger.info("File upload request...")
    if request.method == "POST":
        user_file = request.files["file1"]
        #filename = secure_filename(user_file.filename)
        filename = secure_filename(request.form['filename'])
        app.logger.info("File uploaded")
        file_ext = os.path.splitext(filename)[1]
        if file_ext.lower() not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        user_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        res = make_response(jsonify({"message": filename}), 200)
        return res

    return render_template("public/html/upload-img.html", fortune=fortune())

@app.errorhandler(404)
def page_not_found(error):
    return render_template('public/html/404.html', fortune=fortune()), 404

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = request.form['email']
    if request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

@app.route('/protected')
@flask_login.login_required
def protected():
    return render_template('public/html/upload-img.html')
