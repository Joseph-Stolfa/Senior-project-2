import machine
import utime
import uos
import gc
import ucsv
import adafruit_bno055
import adafruit_gps

# Set up I2C communication with BNO055 IMU
i2c = machine.I2C(0, scl=machine.Pin(3), sda=machine.Pin(2))
imu = adafruit_bno055.BNO055_I2C(i2c)

# Set up UART communication with GPS module
uart = machine.UART(1, baudrate=9600, tx=machine.Pin(4), rx=machine.Pin(5))
gps = adafruit_gps.GPS(uart)

# Set up UART communication with HC-05 Bluetooth module
radio_uart = machine.UART(2, baudrate=9600, tx=machine.Pin(8), rx=machine.Pin(9))

# Set up USB serial communication
usb_serial = machine.UART(0, baudrate=115200, tx=machine.Pin(1), rx=machine.Pin(0))

# Open file for writing GPS and IMU data
filename = "gps_imu_data.csv"
if not uos.path.exists(filename):
    with open(filename, 'w', newline='') as file:
        writer = ucsv.writer(file)
        writer.writerow(["Timestamp", "Latitude", "Longitude", "Heading", "Roll", "Pitch"])

while True:
    # Get GPS data
    gps.update()
    if gps.has_fix:
        timestamp = utime.monotonic()
        latitude = gps.latitude
        longitude = gps.longitude
    else:
        timestamp = None
        latitude = None
        longitude = None

    # Get IMU data
    heading, roll, pitch = imu.euler()

    # Write data to CSV file
    with open(filename, 'a', newline='') as file:
        writer = ucsv.writer(file)
        writer.writerow([timestamp, latitude, longitude, heading, roll, pitch])

    # Send data over radio UART
    radio_uart.write("{}, {}, {}\n".format(latitude, longitude, heading).encode())

    # Send data over USB serial
    usb_serial.write("{}, {}, {}, {}, {}, {}\n".format(timestamp, latitude, longitude, heading, roll, pitch).encode())

    gc.collect()
    utime.sleep(1.0)
