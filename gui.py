# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'converter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 415, 81))
        self.frame.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 10, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.input_currency.setGeometry(QtCore.QRect(40, 120, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.input_currency.setFont(font)
        self.input_currency.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.input_currency.setText("")
        self.input_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.input_currency.setObjectName("input_currency")
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(40, 210, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(40, 300, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.output_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.output_currency.setObjectName("output_currency")
        self.output_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.output_amount.setGeometry(QtCore.QRect(40, 390, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.output_amount.setFont(font)
        self.output_amount.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.output_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.output_amount.setObjectName("output_amount")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(124, 480, 191, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Конвертер валют"))
        self.pushButton.setText(_translate("MainWindow", "конвертация"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
