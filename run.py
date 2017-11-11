#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-11 15:32:08
# @Author  : bitwater (bitwater1997@gmail.com)
# @Link    : http://bitwater1997.cn
# @Version : $Id$

# import os
from app import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
