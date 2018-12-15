from flask import Flask, json, make_response
app = Flask(__name__)

pins = [False for _ in range(1, 9)]


@app.route('/')
def hello():
    return 'Hello world!'


@app.route('/pins/<int:pin>/toggle')
def toggle(pin):
    if 0 < pin <= len(pins):
        response = json.jsonify(pin=pin, status='success')
        pins[pin - 1] = not pins[pin - 1]
    else:
        response = make_response(json.jsonify(
            pin=pin, status='error', error='Pin {} is not supported! Use pins 1-8.'.format(pin)), 404)
    return response


@app.route('/pins/')
def pins_state():
    response = json.jsonify(pins=pins)
    return response


@app.route('/pins/<int:pin>')
def pin_state(pin):
    if 0 < pin <= len(pins):
        response = json.jsonify(pin=pin, state=pins[pin - 1])
    else:
        response = make_response(json.jsonify(
            pin=pin, status='error', error='Pin {} is not supported! Use pins 1-8.'.format(pin)), 404)
    return response
