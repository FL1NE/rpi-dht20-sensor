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
```
cd rpi-dht20-sensor
python -m venv .venv
```

Activate venv
`source .venv/bin/activate`

Install requirements.txt
`pip3 install -r requirements.txt`

## RUN (Get data)

Make sure activate venv before run

`python3 rpi-dht20-sensor.py`

If you want watch, just use `watch`

`watch python3 rpi-dht20-sensor.py`


## Reference

https://raspi-school.com/dht-20/
