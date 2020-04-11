from flask import Flask
from config import Config

app = Flask(__name__)
app.run(debug=True)

app.config.from_object(Config)

from app import routes