import busio
import time
import board
import digitalio
import adafruit_bno055
import adafruit_gps
import sdcardio
import storage
# import os

# Set up I2C
I2C_SCL = board.GP3
I2C_SDA = board.GP2
I2C = busio.I2C(I2C_SCL, I2C_SDA)

# Set up IMU
IMU = adafruit_bno055.BNO055_I2C(I2C, address=0x28)

# Set up GPS
GPS = adafruit_gps.GPS_GtopI2C(I2C, address=0x10)
# Turn on the basic GGA and RMC info (what you typically want)
GPS.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
GPS.send_command(b"PMTK220,1000")

# Set up Radio
radio_tx = board.GP0
radio_rx = board.GP1
radio = busio.UART(radio_tx, radio_rx, baudrate=9600)

# initializes sd card and its form of storage
spi = busio.SPI(clock=board.GP10, MOSI=board.GP11, MISO=board.GP12)
cs = board.GP13
sd = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sd)
storage.mount(vfs, '/sd')

# test bootup
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
time.sleep(30)
led.value = False
time.sleep(.250)

timestamp = time.monotonic()
while True:
    if radio.in_waiting > 0:
        radio_data = radio.read()

        if "on" in radio_data:
            led.value = True
            time.sleep(0.5)

            # LED function
            print("LED on \n")
            radio.write("LED on \n".encode())

            with open("/sd/Data.csv", "w") as file:
                file.write("Latitude, Longitude, "
                           "Altidtude, Satellites,"
                           "Gyro_x, Gyro_y, Gyro_z,"
                           "Accel_x, Accel_y, Accel_z,"
                           "Mag_x, Mag_y, Mag_z\n")

            while "stop" not in radio_data:

                # IMU function
                gyro_x, gyro_y, gyro_z = IMU.gyro
                # Read the acceleration data
                accel_x, accel_y, accel_z = IMU.acceleration
                # Read the magnetic field data
                mag_x, mag_y, mag_z = IMU.magnetic

                # Update GPS
                GPS.update()

                # Test for GPS fix
                if not GPS.has_fix:
                    print('\nNo GPS Fix')
                    continue

                # test csv file and output through usb serial connection
                altitude = ""
                satellites = ""
                latitude = ""
                longitude = ""

                # Checks if any value is None in GPS
                if GPS.latitude is not None:
                    latitude = "{:.6f}".format(GPS.latitude)
                else:
                    latitude = "N/A"

                if GPS.longitude is not None:
                    longitude = "{:.6f}".format(GPS.longitude)
                else:
                    longitude = "N/A"

                if GPS.altitude_m is not None:
                    altitude = "{:.2f}".format(GPS.altitude_m)
                else:
                    altitude = "N/A"

                if GPS.satellites is not None:
                    satellites = "{}".format(GPS.satellites)
                else:
                    satellites = "N/A"

                print("\nLatitude= {0}, Longitude= {1}, "
                      "\nAltidtude= {2}, Satellites {3}\n".format(
                                latitude, longitude,
                                altitude, satellites))
                radio.write("\nLatitude= {0}, Longitude= {1}, "
                            "\nAltidtude= {2}, Satellites {3}\n".format(
                                latitude, longitude,
                                altitude, satellites).encode())
                time.sleep(0.1)

                print("\nGyro: {}, {}, {}\n"
                      "Mag: {}, {}, {}\n"
                      "Accel: {}, {}, {}\n".format(
                            gyro_x, gyro_y, gyro_z,
                            mag_x, mag_y, mag_z,
                            accel_x, accel_y, accel_y))
                radio.write("\nGyro: {}, {}, {}\n"
                            "Mag: {}, {}, {}\n"
                            "Accel: {}, {}, {}\n".format(
                                gyro_x, gyro_y, gyro_z,
                                mag_x, mag_y, mag_z,
                                accel_x, accel_y, accel_y).encode())

                time.sleep(0.1)
                with open("/sd/Data.csv", "a") as file:
                    file.write("{0}, {1}, {2}, {3}, "
                               "{4}, {5}, {6}, "
                               "{7}, {8}, {9}, "
                               "{10}, {11}, {12}\n".format(
                                latitude, longitude,
                                altitude, satellites,
                                gyro_x, gyro_y, gyro_z,
                                mag_x, mag_y, mag_z,
                                accel_x, accel_y, accel_y))
                if radio.in_waiting > 0:
                    radio_data = radio.read()

        elif "off" in radio_data:
            led.value = False
            time.sleep(0.5)
            print("LED off \n")
            radio.write("LED off \n".encode())

