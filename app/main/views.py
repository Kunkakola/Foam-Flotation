#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-11 14:36:06
# @Author  : bitwater (bitwater1997@gmail.com)
# @Link    : http://bitwater1997.cn
# @Version : $Id$

from ..Eigenvalue import Eigenvalue
from . import main_page
import cv2


@main_page.route('/')
def root():
    vc = cv2.VideoCapture(0)
    ret, frame = vc.read()
    vc.release()
    return Eigenvalue(image=frame).run()
