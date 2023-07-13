from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)
db = SQLAlchemy(app)

# This import is at the bottom to avoid circular imports
from app import views, models
