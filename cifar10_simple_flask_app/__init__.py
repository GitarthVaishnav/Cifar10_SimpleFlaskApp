from flask import Flask

app = Flask(__name__)

from cifar10_simple_flask_app import views
