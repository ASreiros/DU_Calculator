from app import app
from flask import render_template, jsonify, request, make_response,  send_file, json
from app import calculate
from app import daily


@app.route("/")
def home():
    return render_template("public/index.html")

@app.route("/calculate", methods=["POST"])
def calculate_salary():
    req = request.get_json()
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
        answer = make_response(jsonify({'message':"JSON received, but nothing was done,wrong id"}, 200))

    return answer


@app.route("/getpdf/<data>")
def provide_pdf(data):
    info = json.loads(data)
    pdf = calculate.create_pdf(info)
    return send_file(pdf, as_attachment=True)


@app.route("/dienpinigiai")
def dienpinigiai():
    daily_dict = daily.provide_dict()
    return render_template("public/daily.html", data=daily_dict)

@app.route("/countallowance", methods=["POST"])
def count_allowance():
    req = request.get_json()
    data = {
        'data': daily.count_daily(req)
    }
    answer = make_response(jsonify(data, 200))
    return answer
