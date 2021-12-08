import os
import random
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
import markdown
import flask_login
from logging.config import dictConfig
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
with open('routes/auth_key.secret', 'r') as fh:
    key = fh.read()
    app.secret_key = key

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

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
        return render_template('public/html/index.html')

@app.route("/external-docs")
def external_docs():
        return render_template('public/html/external-docs.html')

@app.route("/external-parts")
def external_parts():
        return render_template('public/html/external-parts.html')

@app.route("/brochure-art")
def art_ep():
        art_folder = 'img/brochure'
        filenames = os.listdir(os.path.join(app.static_folder, art_folder))
        paths = [url_for('static', filename=os.path.join(art_folder, f)) for f in filenames]
        random.shuffle(paths)
        return render_template('public/html/brochure-art.html', art=paths)

@app.route("/turboninjas")
def turboninjas():
        return render_template('public/html/turboninjas.html')

@app.route("/mk3supra/<path:subpath>")
def serve_turboninjas_files(subpath):
        return send_from_directory(app.static_folder, os.path.join('turboninjas', subpath))

@app.route("/writeups")
def writeups_index():
        return render_template('public/html/writeups-index.html')

@app.route("/tuning")
def tuning():
        return render_template('public/html/tuning.html')

@app.route("/writeups/<path:subpath>")
def writeups_page(subpath):
    path = os.path.join('templates/public/markdown', subpath + '.md')
    if os.path.exists(path):
        md = render_template('public/markdown/' + subpath + '.md')
        html = markdown.markdown(md)
        return render_template("public/html/writeup-template.html", title=subpath, content=html)
    return render_template('public/html/404.html'), 404

@app.route("/upload-img", methods=["GET", "POST"])
def img_upload():
    app.logger.info("File upload request...")
    if request.method == "POST":
        user_file = request.files["file1"]
        app.logger.info("File uploaded")
        app.logger.info(user_file)
        res = make_response(jsonify({"message": user_file.filename}), 200)
        return res

    return render_template("public/html/upload-img.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('public/html/404.html'), 404

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
