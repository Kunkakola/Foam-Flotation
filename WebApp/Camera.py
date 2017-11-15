#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-14 15:00:18
# @Author  : bitwater (bitwater1997@gmail.com)
# @Link    : http://bitwater1997.cn
# @Version : $Id$

import cv2


class Camera(object):

    def __init__(self):
        self.ca = cv2.VideoCapture(0)

    def __del__(self):
        self.ca.release()

    def get_frame(self):
        ret, frame = self.ca.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return frame, jpeg.tobytes()
