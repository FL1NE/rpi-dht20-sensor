#!/usr/bin/env python3
import time
import json
import board
import adafruit_ahtx0

i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

data = {
    "temperature": sensor.temperature,
    "humidity": sensor.relative_humidity
}
print(json.dumps(data, ensure_ascii=False))
