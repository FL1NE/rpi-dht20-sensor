# rpi-dht20-sensor
DHT20 Temperature &amp; Humidity sensor connection for Raspberry Pi

## Setup

### Enable I2C interface

Change setting via raspi-config
`sudo raspi-config`
3 Interface Options > I5 I2C > Enable

### Clone repository

Install `git` if not installed
`sudo apt install -y git`

Clone repository
`git clone https://github.com/FL1NE/rpi-dht20-sensor.git`

### Connect Sensor (Raspberry Pi & DHT20)

Raspberry Pi : DHT10
- VDD : 3.3V
- GPIO 2 : SDA
- GPIO 3 : SCL
- GND : GND

### Install Python 3

`apt install -y python3`

### Setup Python venv / activate venv / install related packages

Setup venv
`python -m venv rpi-dht20-sensor`

Activate venv
`source rpi-dht20-sensor/bin/activate`

Install related packages
`pip3 install adafruit-circuitpython-ahtx0 board rpi.gpio`

## RUN (Get data)

`python3 rpi-dht20-sensor.py`


## Reference

https://raspi-school.com/dht-20/
