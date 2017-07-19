from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging

GPIO.setmode(GPIO.BOARD)

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def launch():
    return statement('Ready to accept a command.')

@ask.intent('GPIOControlIntent', mapping={'status': 'status', 'pin': 'pin'})
def gpio_control(status, pin):

    try:
        pinNum = int(pin)
    except Exception as e:
        return statement('Pin number not valid.')

    GPIO.setup(pinNum, GPIO.OUT)

    if status in ['on', 'high']:    GPIO.output(pinNum, GPIO.HIGH)
    if status in ['off', 'low']:    GPIO.output(pinNum, GPIO.LOW)

    return statement('Turning pin {} {}'.format(pin, status))

@ask.intent('LocationControlIntent', mapping={'status': 'status', 'location': 'location'})
def location_control(status, location):

    locationDict = {
        'light': 11,
	'led': 11
    }

    targetPin = locationDict[location]

    GPIO.setup(targetPin, GPIO.OUT)

    if status in ['on', 'high']:        GPIO.output(targetPin, GPIO.HIGH)
    if status in ['off', 'low']:        GPIO.output(targetPin, GPIO.LOW)

    return statement('Turning {} {}!'.format(location, status))
if __name__ == '__main__':
  port = 5000 #the custom port you want
  app.run(host='0.0.0.0', port=port)
