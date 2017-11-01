# Configure the Raspberry Pi Zero W as a sensor module

## O/S

Install Raspbian Stretch

## Python Modules

This demo uses Python 2.7.13 which is the default install for Raspbian Stretch

### Install the RPi.GPIO Module

`
sudo apt-get install python-dev python-rpi.gpio
`

### Install the Adafruit Python GPIO Library

`
sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus git
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python setup.py install
`

### Download the Adafruit Python BME280 Library

`
git clone https://github.com/adafruit/Adafruit_Python_BME280
`

Note you'll need to have the `Adafruit_BME280.py` file in the same folder or a referenced folder