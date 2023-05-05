from app import app
from flask import render_template, jsonify, request, make_response
from app import calculate


@app.route("/")
def home():
    data = {
        'hour_netto': 0,
        'hour_brutto': 0,
        'hours': 160,
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

@app.route("/calculate", methods=["POST"])
def calculate_salary():
    req = request.get_json()
    print(req)
    if req['id'] == 'amount-brutto':
        data = {
            'data': calculate.calculate_netto(req)
        }
        answer = make_response(jsonify(data, 200))
    elif req['id'] == 'amount-netto':
        data = {
            'data': calculate.calculate_brutto(req)
        }
        answer = make_response(jsonify(data, 200))
    elif req['id'] == 'amount-netto-hour':
        data = {
            'data': calculate.calculate_brutto_hour(req)
        }
        answer = make_response(jsonify(data, 200))
    elif req['id'] == 'amount-brutto-hour':
        data = {
            'data': calculate.calculate_netto_hour(req)
        }
        answer = make_response(jsonify(data, 200))
    else:
        print(req['id'])
        answer = make_response(jsonify({'message':"JSON received, but nothing was done,wrong id"}, 200))

    return answer
