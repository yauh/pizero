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
