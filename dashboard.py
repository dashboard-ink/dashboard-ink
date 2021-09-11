#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os

import logging
import sys
lib_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
core_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'core')
if os.path.exists(lib_dir):
    sys.path.append(lib_dir)

if os.path.exists(core_dir):
    sys.path.append(core_dir)

from waveshare_epd import epd7in5b_HD
from core import fonts
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

    # Drawing on the Vertical image
    logging.info("Drawing dashboard...")
    black_image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    red_image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw_black_image = ImageDraw.Draw(black_image)
    draw_red_image = ImageDraw.Draw(red_image)

    current_date = datetime.now()

    draw_black_image.text((2, 0), current_date.strftime('%Y-%m-%d'), font = fonts.font24, fill = 0)
    draw_black_image.text((100, 0), 'Updated at' + current_date.strftime("%Y-%m-%d %H:%M:%S"), font = fonts.font12, fill = 0)
    draw_red_image.text((2, 30), '7.5inch epd', font = fonts.font18, fill = 0)
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
