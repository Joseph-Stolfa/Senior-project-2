import board
import busio
import sdcardio
import storage
import time
import os

time.sleep(1)
# test usb serial conbection
print('testing usb serial')

# initializes sd card and its form of storage
spi = busio.SPI(clock=board.GP18, MOSI=board.GP19, MISO=board.GP20)
cs = board.GP21
sd = sdcardio.SDCard(spi, cs)

vfs = storage.VfsFat(sd)
storage.mount(vfs, '/sd')


# test usb serial conbection
print(os.listdir('/sd'))

# test csv file and output through usb serial connection
with open("/sd/testfile.txt", "w") as file:
    file.write("1. Hello, world!\r\n")
    print(file.read())

while True:
    print('end')
    time.sleep(10)
