from re import A
from flask import Flask

app = Flask(__name__)

from balance import routes