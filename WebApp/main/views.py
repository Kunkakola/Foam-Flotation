#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-11 14:36:06
# @Author  : bitwater (bitwater1997@gmail.com)
# @Link    : http://bitwater1997.cn
# @Version : $Id$

from flask import render_template, g
from ..Eigenvalue import Eigenvalue
from ..Camera import Camera
from . import main_page


@main_page.before_request
def before_request():
    g.frame, g.jpeg = gen(Camera()).next()


@main_page.route('/')
def root():
    ei = Eigenvalue(image=g.frame)
    return render_template('/main/index.html', eigenvalue=ei.run())


@main_page.route('/img')
def img():
    return g.jpeg


def gen(camera):
    while True:
        frame, jpeg = camera.get_frame()
        yield (frame, jpeg)
