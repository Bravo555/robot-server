from socket import socket, AF_INET, SOCK_DGRAM
from gpiozero import LED
from PCA9685 import PCA9685

PORT = 12345  # arbitrary, just make it match in Android code
IP = "0.0.0.0"  # represents any IP address

led_pins = [2, 17, 10]
leds = [LED(i) for i in led_pins]
servo = PCA9685(0x40, debug=False)
servo.setPWMFreq(50)

sock = socket(AF_INET, SOCK_DGRAM)  # SOCK_DGRAM means UDP socket
sock.bind((IP, PORT))

while True:
    print("Waiting for data...")
    data, addr = sock.recvfrom(2)  # blocking
    address, state = data

    print('received: ')
    print(data)
    # address: 1-3 LEDs, 255 is servo
    if address in range(0x0, 0x02):
        if state == 0x0:
            leds[address].off()
        else:
            leds[address].on()
    elif address == 0xff:
        pass
