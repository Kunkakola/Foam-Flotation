#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-10 13:45:00
# @Author  : bitwater (bitwater1997@gmail.com)
# @Link    : http://bitwater1997.cn
# @Version : $Id$

import cv
import cv2
import math


class Eigenvalue(object):
    """docstring for Eigenvalue"""

    def __init__(self, image_dir=None, image=None):
        self.image_dir = image_dir
        # image = cv2.imread(self.image_dir,cv.CV_LOAD_IMAGE_GRAYSCALE)
        self.image = image if image_dir is None else cv2.imread(self.image_dir)
        self.gray_Freq = []
        for i in range(0, 256):
            self.gray_Freq.append(0)

    def run(self):
        self.gray_average = 0
        self.tran_IMgrad()
        self.cal_IMentropy()
        self.cal_IMenergy()
        self.cal_IMmoment()
        return 'gray_average = %d,\n\
                entropy = %d,\n\
                energy = %d,\n\
                hu_moments = %s ' % (
            self.gray_average,
            self.entropy,
            self.energy,
            str(self.hu_moments)
        )

    def test(self):
        print "gray_average", self.gray_average
        print "entropy", self.entropy
        print "energy", self.energy
        # print "hu_moments", [math.log(abs(x), 2) for x in self.hu_moments]
        print "hu_moments", self.hu_moments

    def tran_IMgrad(self):
        image = self.image
        gray_sum = 0
        size = image.shape
        for i in xrange(size[0]):
            for j in xrange(size[1]):
                gray_value = 0.3 * image[i, j, 0] + 0.59 * \
                    image[i, j, 1] + 0.11 * image[i, j, 2]
                gray_sum += gray_value
                self.gray_Freq[int(gray_value)] += 1.0
        self.gray_average = gray_sum / (size[0] * size[1])
        for i in xrange(0, 256):
            self.gray_Freq[i] /= size[0] * size[1]

    def cal_IMentropy(self):
        self.entropy = 0
        for i in xrange(0, 256):
            if self.gray_Freq[i] != 0:
                self.entropy -= self.gray_Freq[i] * \
                    math.log(self.gray_Freq[i], 2)

    def cal_IMenergy(self):
        self.energy = 0
        for i in xrange(0, 256):
            self.energy += math.pow(self.gray_Freq[i], 2)

    def cal_IMmoment(self):
        image = cv2.cvtColor(self.image, cv.CV_RGB2GRAY)
        self.moments = cv2.moments(image)
        self.hu_moments = cv2.HuMoments(self.moments)


if __name__ == '__main__':
    ei = Eigenvalue(image_dir='../new.jpg')
    ei.run()
    ei.test()
