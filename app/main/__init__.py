#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-11 14:35:34
# @Author  : bitwater (bitwater1997@gmail.com)
# @Link    : http://bitwater1997.cn
# @Version : $Id$

from flask import Blueprint
main_page = Blueprint('main_page', __name__,
                      # template_folder='templates',
                      # static_folder='static'
                      )
from views import *
