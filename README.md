# pizero
My Pi Zero projects

## Hardware

I have a Pi Zero WH with a [2.23 OLED display](https://www.waveshare.com/2.23inch-oled-hat.htm).

## scanner.py

Run a Wifi scanner (SSID/quality) and output data to the OLED display.

### Running

Copy `scanner.py`, font and `drive` folder to the raspberry pi. Install Python 3 and the [wifi package](https://pypi.org/project/wifi/).

the program must run as root, i.e.

`$ sudo python scanner.py`

## BME680

In order to get the environmental sensor BME680 running do the following:

```
raspi-config nonint do_i2c 0
apt install -y python3-smbus i2c-tools
apt install python3-pip -y
pip3 install --user adafruit-circuitpython-bme680
pip3 install --user paho-mqtt
```

Connect with 4 wires, using I2C

| Raspberry Pi GPIO | BME280 | Color |
| --- | --- | --- |
| 1 (3v3 power) | VCC | black |
| 6 (Ground) | GND | brown |
| 5 (GPIO3 / SCL) | SCL | red |
| 3 (GPIO2 / SDA) | SDA | orange |