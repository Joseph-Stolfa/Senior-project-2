import machine
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT


radio = machine.UART(0, 9600)

while True:
    if radio.any() > 0:
        data = radio.read()
        print(data)

    if "on" in data:
        led.value = True
        time.sleep(0.5)
        print('LED on \n')
        radio.write('LED on \n')

    elif "off" in data:
        led.value = False
        time.sleep(0.5)
        print('LED off \n')
        radio.write('LED off \n')
        # Write your code here :-)
