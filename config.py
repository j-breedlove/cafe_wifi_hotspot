import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app/hotspot.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'Un*hr$2vx^WBpNsJ*a3w'
