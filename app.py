from socket import socket, AF_INET, SOCK_DGRAM
from gpiozero import LED

PORT = 12345  # arbitrary, just make it match in Android code
IP = "0.0.0.0"  # represents any IP address

led_pins = [2, 17, 10]
leds = [LED(i) for i in led_pins]

sock = socket(AF_INET, SOCK_DGRAM)  # SOCK_DGRAM means UDP socket
sock.bind((IP, PORT))

while True:
    print("Waiting for data...")
    data, addr = sock.recvfrom(2)  # blocking
    pin, state = data
    print('received: ')
    print(data)
    if state == 0x0:
        leds[pin].off()
    else:
        leds[pin].on()