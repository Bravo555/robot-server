#!/usr/bin/python3

from socket import socket, AF_INET, SOCK_DGRAM
from gpiozero import LED
from PCA9685 import PCA9685
import sys

PORT = 12345  # arbitrary, just make it match in Android code
IP = "0.0.0.0"  # represents any IP address

led_pins = [17, 27, 22]
leds = [LED(i) for i in led_pins]
servo = PCA9685(0x40, debug=False)
servo.setPWMFreq(125)

sock = socket(AF_INET, SOCK_DGRAM)  # SOCK_DGRAM means UDP socket
sock.bind((IP, PORT))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Using default port:', PORT)
    elif len(sys.argv) == 2:
        try:
            PORT = int(sys.argv[1])
            print('Using specified port:', PORT)
        except ValueError:
            print('Wrong port (0-65535)!')
            print('Usage: ./app.py [port=12345]')
            sys.exit(1)
    else:
        print('Wrong arguments!')
        print('Usage: ./app.py [port=12345]')
        sys.exit(1)

    while True:
        print("Waiting for data...")
        data, addr = sock.recvfrom(2)  # blocking
        address, state = data

        print('received: ')
        print(data.hex())
        # address: 1-3 LEDs, 255-240 is servo
        if address in range(0x0, 0x03):
            if state == 0x0:
                leds[address].off()
            else:
                leds[address].on()
        elif address in range(0xf0, 0xff + 1):
            channel = 0xff - address
            time = int(1001 + 3.921 * state)
            servo.setServoPulse(channel, time)
