import werkzeug.serving
from routes.main import app

def run_server():
    werkzeug.run_simple(application=app, hostname='127.0.0.1', port=1989, use_reloader=True)

if __name__ == '__main__':
    run_server()
