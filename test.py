# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lcd_weather.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(807, 562)
        mainForm.setStyleSheet("#mainForm{\n"
"background-image: url(:/image/sky_blue2.jpeg) 0 0 0 0 stretch stretch;\n"
"}\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(mainForm)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(mainForm)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(6)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(114, 159, 207);\n"
"background-color: rgb(3, 119, 255);\n"
"color: rgb(255, 255, 255);")
        self.label.setText("풍향")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10% \"Cantarell\";")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(mainForm)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("background-color: rgb(114, 159, 207);\n"
"background-color: rgb(3, 119, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_9.setText("?")
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10% \"Cantarell\";")
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.gridLayout_2.addWidget(self.frame_6, 3, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(mainForm)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("background-color: rgb(204, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setText("현재온도")
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10% \"Cantarell\";")
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(mainForm)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("background-color: rgb(114, 159, 207);\n"
"background-color: rgb(3, 119, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setText("강수량")
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10% \"Cantarell\";")
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.gridLayout_2.addWidget(self.frame_5, 3, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(mainForm)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.frame_7)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("background-color: rgb(114, 159, 207);\n"
"background-color: rgb(3, 119, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_11.setText("습도")
        self.label_11.setTextFormat(QtCore.Qt.RichText)
        self.label_11.setScaledContents(True)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10% \"Cantarell\";")
        self.label_12.setTextFormat(QtCore.Qt.RichText)
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.gridLayout_2.addWidget(self.frame_7, 0, 2, 1, 1)
        self.frame_8 = QtWidgets.QFrame(mainForm)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.frame_8)
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet("background-color: rgb(114, 159, 207);\n"
"background-color: rgb(3, 119, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_13.setText("최저온도")
        self.label_13.setTextFormat(QtCore.Qt.RichText)
        self.label_13.setScaledContents(True)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_7.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10% \"Cantarell\";")
        self.label_14.setTextFormat(QtCore.Qt.RichText)
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.gridLayout_2.addWidget(self.frame_8, 1, 2, 1, 1)
        self.frame_9 = QtWidgets.QFrame(mainForm)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.frame_9)
        self.label_15.setAutoFillBackground(False)
        self.label_15.setStyleSheet("background-color: rgb(114, 159, 207);\n"
"background-color: rgb(3, 119, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_15.setText("적설량")
        self.label_15.setTextFormat(QtCore.Qt.RichText)
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10% \"Cantarell\";")
        self.label_16.setTextFormat(QtCore.Qt.RichText)
        self.label_16.setScaledContents(True)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_8.addWidget(self.label_16)
        self.gridLayout_2.addWidget(self.frame_9, 3, 2, 1, 1)
        self.frame_3 = QtWidgets.QFrame(mainForm)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color: rgb(114, 159, 207);\n"
"background-color: rgb(3, 119, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setText("풍속")
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10% \"Cantarell\";")
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(mainForm)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setAutoFillBackground(False)
        self.label_17.setStyleSheet("background-color: rgb(114, 159, 207);\n"
"background-color: rgb(3, 119, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_17.setText("최고온도")
        self.label_17.setTextFormat(QtCore.Qt.RichText)
        self.label_17.setScaledContents(True)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_9.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10% \"Cantarell\";")
        self.label_18.setTextFormat(QtCore.Qt.RichText)
        self.label_18.setScaledContents(True)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_9.addWidget(self.label_18)
        self.gridLayout_2.addWidget(self.frame_2, 1, 1, 1, 1)

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "Weather report"))
        self.label_2.setText(_translate("mainForm", "sample"))
        self.label_10.setText(_translate("mainForm", "sample"))
        self.label_6.setText(_translate("mainForm", "sample"))
        self.label_8.setText(_translate("mainForm", "sample"))
        self.label_12.setText(_translate("mainForm", "sample"))
        self.label_14.setText(_translate("mainForm", "sample"))
        self.label_16.setText(_translate("mainForm", "sample"))
        self.label_4.setText(_translate("mainForm", "sample"))
        self.label_18.setText(_translate("mainForm", "sample"))
