#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-15 20:07:34
# @Author  : bitwater (bitwater1997@gmail.com)
# @Link    : http://bitwater1997.cn
# @Version : $Id$

from PyQt5 import QtCore, QtGui, QtWidgets
from PcApp.mainWindow import MainWindow
import sys

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
