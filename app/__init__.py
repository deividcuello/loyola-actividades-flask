from flask import Flask

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Reemplaza 'your_secret_key' con tu propia clave secreta

from app import routes