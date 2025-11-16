#!/usr/bin/python3
import board
from busio import I2C
import adafruit_bme680
import paho.mqtt.client as mqtt
import time

# set the variables
broker='yourmqtt.host.local'
port=1883
publish_topic="pizero/bme680"
clientid='pizero'
username='yourusername'
password='yourpassword'
insecure=True
qos=1
retain_message=True

# Create library object using our Bus I2C port
i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.2

# You will usually have to add an offset to account for the temperature of
# the sensor. This is usually around 5 degrees but varies by use. Use a
# separate temperature sensor to calibrate this one.
#temperature_offset = -5
temperature_offset = -1

#MQTT Connection
client=mqtt.Client(clientid)
client.username_pw_set(username, password)
client.connect(broker, port)
client.loop_start()

while True:
    client.publish("{}/temperature".format(publish_topic),"{:.2f}".format((bme680.temperature + temperature_offset)),qos,retain_message)
    client.publish("{}/humidity".format(publish_topic),"{:.2f}".format(bme680.humidity),qos,retain_message)
    client.publish("{}/rel_humidity".format(publish_topic),"{:.2f}".format(bme680.relative_humidity),qos,retain_message)
    client.publish("{}/pressure".format(publish_topic),"{:.2f}".format(bme680.pressure),qos,retain_message)
    client.publish("{}/altitude".format(publish_topic),"{:.2f}".format(bme680.altitude),qos,retain_message)
    client.publish("{}/gas".format(publish_topic),"{:.2f}".format(bme680.gas),qos,retain_message)
    time.sleep(30)

client.disconnect()
client.loop_stop()