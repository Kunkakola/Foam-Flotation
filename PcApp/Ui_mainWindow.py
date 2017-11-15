# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/bitwater/Desktop/Foam-Flotation/PcApp/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 642)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton_start = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_start.setGeometry(QtCore.QRect(780, 580, 94, 26))
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(670, 70, 271, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lineEdit_gray_average = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_gray_average.setReadOnly(True)
        self.lineEdit_gray_average.setObjectName("lineEdit_gray_average")
        self.horizontalLayout_2.addWidget(self.lineEdit_gray_average)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lineEdit_entropy = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_entropy.setObjectName("lineEdit_entropy")
        self.horizontalLayout_3.addWidget(self.lineEdit_entropy)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(85, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lineEdit_energy = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_energy.setObjectName("lineEdit_energy")
        self.horizontalLayout.addWidget(self.lineEdit_energy)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.lineEdit_hu_moments = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_hu_moments.setObjectName("lineEdit_hu_moments")
        self.horizontalLayout_4.addWidget(self.lineEdit_hu_moments)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label_image = QtWidgets.QLabel(self.centralWidget)
        self.label_image.setGeometry(QtCore.QRect(20, 40, 531, 381))
        self.label_image.setObjectName("label_image")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_start.setText(_translate("MainWindow", "start"))
        self.label_2.setText(_translate("MainWindow", "gray_average"))
        self.label_3.setText(_translate("MainWindow", "entropy"))
        self.label.setText(_translate("MainWindow", "energy"))
        self.label_4.setText(_translate("MainWindow", "hu_moments"))
        self.label_image.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

