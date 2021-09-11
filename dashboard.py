#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os

import logging
import sys
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd7in5b_HD
import time
from datetime import datetime
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
    font12 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 12)

    # Drawing on the Vertical image
    logging.info("Drawing dashboard...")
    black_image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    red_image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw_black_image = ImageDraw.Draw(black_image)
    draw_red_image = ImageDraw.Draw(red_image)

    current_date = datetime.now()

    draw_black_image.text((2, 0), current_date.strftime('%Y-%m-%d'), font = font24, fill = 0)
    draw_black_image.text((100, 0), 'Updated at' + current_date, font = font12, fill = 0)
    draw_red_image.text((2, 20), '7.5inch epd', font = font18, fill = 0)
    epd.display(epd.getbuffer(black_image), epd.getbuffer(red_image))
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
