#!/usr/bin/python

import time
from escpos.printer import Usb
from PIL import Image, ImageFont, ImageDraw

from utils import *

WHITE = 1
BLACK = 0

#p = Usb(0x0483, 0x5720, 0)
image = Image.new('1', (590,400), 1)

#x1 = 0
#y1 = 420

draw = ImageDraw.Draw(image)

productfont32 = font=createfont('freemono',32)
productfont35 = font=createfont('freemonobold',35)

#draw.text((20, 10), 'Welcome to the', fill=BLACK, font=createfont('freemono',18))
draw.text((10, 30), 'Banana', fill=BLACK, font=productfont32)
draw.text((10, 60), 'Croissant', fill=BLACK, font=productfont32)
draw.text((10, 90), 'Kit Kat', fill=BLACK, font=productfont32)
draw.text((10, 120), 'Honey', fill=BLACK, font=productfont32)
draw.text((10, 150), 'Steak', fill=BLACK, font=productfont32)
draw.text((10, 180), 'More Steak', fill=BLACK, font=productfont32)
draw.text((10, 210), 'Chicken filet', fill=BLACK, font=productfont32)
draw.text((10, 240), 'Cat food', fill=BLACK, font=productfont32)

draw.text((450, 280), '------', fill=BLACK, font=productfont32)
draw.text((10, 300), 'TOTAL', fill=BLACK, font=productfont35)
draw.text((450, 320), '------', fill=BLACK, font=productfont32)
draw.text((450, 325), '------', fill=BLACK, font=productfont32)

draw.text((480, 0), 'EUR', fill=BLACK, font=productfont32)

draw.text((460, 30), '1.50', fill=BLACK, font=productfont32)
draw.text((460, 60), '2.50', fill=BLACK, font=productfont32)
draw.text((460, 90), '2.60', fill=BLACK, font=productfont32)
draw.text((460, 120), '0.40', fill=BLACK, font=productfont32)
draw.text((460, 150), '2.40', fill=BLACK, font=productfont32)
draw.text((460, 180), '1.05', fill=BLACK, font=productfont32)
draw.text((460, 210), '3.60', fill=BLACK, font=productfont32)

msg = 324.90
w, h = draw.textsize()
print(w, h)


draw.text(((590-w), 240), msg, fill=BLACK, font=productfont32)
draw.text((460, 300), '2345.90', fill=BLACK, font=productfont32)

image.show()


p.cut()

time.sleep(2)

p.cashdraw(2)
