import flask

app = flask.Flask(__name__)

from app import routes, exceptions, external_requests