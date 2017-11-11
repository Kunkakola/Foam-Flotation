#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-11 14:09:25
# @Author  : bitwater (bitwater1997@gmail.com)
# @Link    : http://bitwater1997.cn
# @Version : $Id$

import os
from flask import Flask
import cv2
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)
# setup the setting
lastdir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
app.config.from_pyfile(os.path.join(lastdir, 'config.py'))

file_handler = RotatingFileHandler(app.config['LOGGING_URI'], 'a',
                                   1 * 1024 * 1024, 10)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('WebSite startup !!!')


from main import main_page
app.register_blueprint(main_page)
