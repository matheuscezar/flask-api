import flask

app = flask.Flask(__name__)

from app.controllers import user, phone, auth