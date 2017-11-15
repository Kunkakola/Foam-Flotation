# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, QTimer, QByteArray
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QImage, QPixmap
from .Ui_mainWindow import Ui_MainWindow
import cv2
from Eigenvalue import Eigenvalue


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.on_image_update)
        self.video = cv2.VideoCapture(0)
        self.image = QImage()

    def __del__(self):
        self.video.release()

    def get_Image(self):
        ret, self.frame = self.video.read()
        ret, self.jpeg = cv2.imencode('.jpg', self.frame)

    def cal_Eigenvalue(self):
        ei = Eigenvalue(image=self.frame)
        ei.run()
        self.gray_average = ei.gray_average
        self.entropy = ei.entropy
        self.energy = ei.energy

    @pyqtSlot()
    def on_image_update(self):
        self.get_Image()
        self.cal_Eigenvalue()
        self.update_EigeLabel()
        im = QByteArray(self.jpeg.tobytes())
        self.image.loadFromData(im)
        self.label_image.setPixmap(QPixmap().fromImage(self.image))

    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        self.timer.start(100)
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

    def update_EigeLabel(self):
        self.lineEdit_energy.setText(str(self.energy))
        self.lineEdit_entropy.setText(str(self.entropy))
        self.lineEdit_gray_average.setText(str(self.gray_average))
