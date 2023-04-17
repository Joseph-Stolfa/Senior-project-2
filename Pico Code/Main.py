import busio
import time
import board
import digitalio
import adafruit_bno055
import adafruit_gps

# test bootup
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
time.sleep(5)
led.value = False
time.sleep(.250)


I2C_SCL = board.GP3
I2C_SDA = board.GP2
I2C = busio.I2C(I2C_SCL, I2C_SDA)

# Set up IMU
IMU = adafruit_bno055.BNO055_I2C(I2C, address=0x28)

# Set up GPS
# GPS_SCL = board.GP7
# GPS_SDA = board.GP6
# GPS_I2C = busio.I2C(GPS_SCL, GPS_SDA)
# GPS = adafruit_gps.GPS_GtopI2C(GPS_I2C)
GPS = adafruit_gps.GPS_GtopI2C(I2C, address=0x10)
# Turn on the basic GGA and RMC info (what you typically want)
GPS.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

# Set up radio
radio_tx = board.GP0 
radio_rx = board.GP1
radio = busio.UART(radio_tx, radio_rx, baudrate=9600)

timestamp = time.monotonic()
while True:
    if radio.in_waiting > 0:
        radio_data = radio.read()
        print(radio_data)
        
        GPS_data = GPS.read(32)  # read up to 32 bytes
        
        if "on" in radio_data:
            led.value = True
            time.sleep(0.5)
            
            # LED function
            print("LED on \n")
            radio.write("LED on \n".encode())
            
            # IMU function
            print("Temp: {}".format(IMU.temperature))
            radio.write("Temp: {} \n".format(IMU.temperature) .encode())
            time.sleep(0.1)
            
            # GPS function
            
            if GPS_data is not None:
                # convert bytearray to string
                data_string = ''.join([chr(b) for b in GPS_data])
                print(data_string, end="")
                radio.write("GPS: {}\n" .format(data_string).encode())
        
        elif "off" in radio_data:
            led.value = False
            time.sleep(0.5)
            print("LED off \n")
            radio.write("LED off \n".encode())
            # Write your code here :-)
