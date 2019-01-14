from flask import Flask, json, make_response
from gpiozero import LED
app = Flask(__name__)

led_pins = [2, 3, 4]

pins = [LED(i) for i in led_pins]


@app.route('/')
def hello():
    return 'Hello world!'


@app.route('/pins/<int:pin>/toggle')
def toggle(pin):
    if 0 < pin <= len(pins):
        response = json.jsonify(pin=pin, status='success')
        pins[pin].toggle()
    else:
        response = make_response(json.jsonify(
            pin=pin, status='error', error='Pin {} is not supported! Use pins 1-8.'.format(pin)), 404)
    return response
