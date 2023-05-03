from app import app
from flask import render_template

@app.route("/")
def home():
    data = {
        'netto': 0,
        'brutto': 0,
        'total': 0,
        'NPD': True,
        'sodra_floor': True,
        'show_settings': False,
        'show_hour': False,
        'citizen': True,
        'term_agreement': True,
        'sodra_group': 1,
        'GPM': 0,
        'PSD': 0,
        'VSD': 0,
        'add': 0,
        'garant': 0,
        'longterm': 0,
        'incident': 0,
        'unemp': 0,
        'floor': 0,
    }
    return render_template("public/index.html", data=data)
