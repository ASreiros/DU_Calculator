from flask import Flask

app = Flask(__name__)

from app import views
from app import BruttoCalculator
from app import calculate
from app import daily