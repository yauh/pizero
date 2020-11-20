import time
import sys
sys.path.append('./drive')
import SPI
import SSD1305

from wifi import Cell, Scheme
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# Raspberry Pi pin configuration:
RST = None # on the PiOLED this pin isnt used
DC = 24
SPI_PORT = 0
SPI_DEVICE = 0

# 128x32 display with hardware SPI:
disp = SSD1305.SSD1305_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 0
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Define a function which adds a summary attribute (this isn't necessary but was handy for my purposes)
def scanForCells():
    # Scan using wlan0
    cells = Cell.all('wlan0')

    return cells

# Load font for display
font = ImageFont.truetype('fixed_01.ttf',8)

while True:
    print('*** Scan at ' + time.strftime("%a, %d %b %Y %H:%M:%S +0000"))

    cells = scanForCells()

    for cell in cells:

        print('SSID {} ({}, Channel {}) / Quality {} / Signal {}db'.format(cell.ssid, cell.frequency, cell.channel, cell.quality, cell.signal))

        LINE1 = str(cell.ssid)
        LINE2 = "C:" + str(cell.channel).zfill(2) + " Q:" + str(cell.quality) + " S:" + str(cell.signal) +"db"
        LINE3 = "========================="
        LINE4 = str(time.strftime("%d/%m/%Y %H:%M:%S"))

        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        # Write two lines of text.
        draw.text((x, top),       LINE1, font=font, fill=255)
        draw.text((x, top+8),     LINE2, font=font, fill=255)
        draw.text((x, top+16),    LINE3, font=font, fill=255)
        draw.text((x, top+25),    LINE4, font=font, fill=255)

        # Display image.
        disp.image(image)
        disp.display()
        time.sleep(3)

    time.sleep(60)
