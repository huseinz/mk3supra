from waitress import serve
from routes.main import app

serve(app, host='localhost', port=1989)
