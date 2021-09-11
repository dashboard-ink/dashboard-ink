#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os

import logging
import sys
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
print(libdir)
if os.path.exists(libdir):
    print('Apending lib path')
    sys.path.append(libdir)

from waveshare_epd import epd7in5b_HD
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in5b_HD Demo")

    epd = epd7in5b_HD.EPD()

    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    font24 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 32)
    font18 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 18)

    # Drawing on the Vertical image
    logging.info("2.Drawing on the Vertical image...")
    Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    Limage_Other = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw_Himage = ImageDraw.Draw(Limage)
    draw_Himage_Other = ImageDraw.Draw(Limage_Other)
    draw_Himage.text((2, 0), '2020-07-12', font = font24, fill = 0)
    draw_Himage.text((2, 20), '7.5inch epd', font = font18, fill = 0)
    draw_Himage_Other.text((20, 50), u'微雪电子', font = font18, fill = 0)
    draw_Himage_Other.line((10, 90, 60, 140), fill = 0)
    draw_Himage_Other.line((60, 90, 10, 140), fill = 0)
    draw_Himage_Other.rectangle((10, 90, 60, 140), outline = 0)
    draw_Himage_Other.line((95, 90, 95, 140), fill = 0)
    draw_Himage.line((70, 115, 120, 115), fill = 0)
    draw_Himage.arc((70, 90, 120, 140), 0, 360, fill = 0)
    draw_Himage.rectangle((10, 150, 60, 200), fill = 0)
    draw_Himage.chord((70, 150, 120, 200), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Limage), epd.getbuffer(Limage_Other))
    time.sleep(10)
    

    logging.info("Clear...")
    epd.init()
    epd.Clear()

    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5b_HD.epdconfig.module_exit()
    exit()