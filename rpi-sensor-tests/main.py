from time import sleep

import RPi.GPIO as GPIO
from Adafruit_BME280 import *

# to use Raspberry Pi board pin numbers
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
# set up the GPIO channels
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

garage_door_state = {0: "Closed", 1: "Open"}
pir_state = {0: "No motion", 1: "Motion"}

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)


while True:
    garage_door_value = GPIO.input(4)
    pir_value = GPIO.input(17)

    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    humidity = sensor.read_humidity()


    print garage_door_value, pir_value, garage_door_state[garage_door_value], pir_state[pir_value]
    print 'Temp      = {0:0.3f} deg C'.format(degrees)
    print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
    print 'Humidity  = {0:0.2f} %'.format(humidity)

    sleep(1)