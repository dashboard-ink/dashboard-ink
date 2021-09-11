#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os

import logging
import sys
lib_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
core_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'core')
plugin_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'plugin_dir')
if os.path.exists(lib_dir):
    sys.path.append(lib_dir)

if os.path.exists(core_dir):
    sys.path.append(core_dir)

if os.path.exists(plugin_dir):
    sys.path.append(plugin_dir)

from waveshare_epd import epd7in5b_HD
from core import fonts
from plugin import title_bar
import time
from PIL import Image,ImageDraw
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("Dashboard demo")

    black_image = Image.new('1', (epd.height, epd.width), 255)
    red_image = Image.new('1', (epd.height, epd.width), 255)
    draw_black_image = ImageDraw.Draw(black_image)
    draw_red_image = ImageDraw.Draw(red_image)
    title_plugin = title_bar.TitleBar(0, 0)
    title_plugin.draw(draw_black_image, draw_red_image)
    epd = epd7in5b_HD.EPD()

    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    # Drawing on the Vertical image
    logging.info("Drawing dashboard...")

    
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
