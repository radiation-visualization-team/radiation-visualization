from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from client.array import Templabel
from client.matrix import Sub_MatrixForm


class SubArray_Form(object):
    def __init__(self, xy):
        self.size_x, self.size_y = xy

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet("background-color:white")
        # self.label = QtWidgets.QLabel(Form)
        self.label = Templabel(Form)
        self.label.setMouseTracking(True)
        self.label.setObjectName("label")

        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setObjectName("pushButton1")

        if (self.size_x, self.size_y) == ('8', '16'):
            Form.setFixedSize(450, 300)
            self.label.setGeometry(QtCore.QRect(0, 0, 450, 280))
            self.pushButton1.setGeometry(QtCore.QRect(177, 250, 100, 30))
            self.label.setPixmap(QtGui.QPixmap("client\\resource\\upper\\8x16.png"))
            self.label.setAlignment(Qt.AlignCenter)

            self.l_1_1 = QtWidgets.QLineEdit(Form)
            self.l_1_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_1_1.setGeometry(187, 89, 80, 20)

        if (self.size_x, self.size_y) == ('8', '32'):
            Form.setFixedSize(820, 290)
            self.label.setGeometry(QtCore.QRect(0, 0, 820, 240))
            self.pushButton1.setGeometry(QtCore.QRect(361, 250, 100, 30))
            self.label.setPixmap(QtGui.QPixmap("client\\resource\\upper\\8x32.png"))
            self.label.setAlignment(Qt.AlignCenter)

            self.l_1_1 = QtWidgets.QLineEdit(Form)
            self.l_2_1 = QtWidgets.QLineEdit(Form)
            self.l_2_2 = QtWidgets.QLineEdit(Form)
            self.l_1_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_2_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_2_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_1_1.setGeometry(380, 47, 60, 20)
            self.l_2_1.setGeometry(142, 141, 60, 20)
            self.l_2_2.setGeometry(620, 141, 60, 20)

        if (self.size_x, self.size_y) == ('16', '16'):
            Form.setFixedSize(610, 490)
            self.label.setGeometry(QtCore.QRect(0, 0, 610, 440))
            self.pushButton1.setGeometry(QtCore.QRect(256, 454, 100, 30))
            self.label.setPixmap(QtGui.QPixmap("client\\resource\\upper\\16x16.png"))
            self.label.setAlignment(Qt.AlignCenter)

            self.l_1_1 = QtWidgets.QLineEdit(Form)
            self.l_2_1 = QtWidgets.QLineEdit(Form)
            self.l_2_2 = QtWidgets.QLineEdit(Form)
            self.l_1_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_2_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_2_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_1_1.setGeometry(277, 117, 60, 20)
            self.l_2_1.setGeometry(206, 245, 60, 20)
            self.l_2_2.setGeometry(351, 245, 60, 20)

        if (self.size_x, self.size_y) == ('16', '32'):
            Form.setFixedSize(970, 440)
            self.label.setGeometry(QtCore.QRect(0, 0, 970, 390))
            self.pushButton1.setGeometry(QtCore.QRect(437, 392, 100, 30))
            self.label.setPixmap(QtGui.QPixmap("client\\resource\\upper\\16x32.png"))
            self.label.setAlignment(Qt.AlignCenter)

            self.l_1_1 = QtWidgets.QLineEdit(Form)
            self.l_2_1 = QtWidgets.QLineEdit(Form)
            self.l_2_2 = QtWidgets.QLineEdit(Form)
            self.l_3_1 = QtWidgets.QLineEdit(Form)
            self.l_3_2 = QtWidgets.QLineEdit(Form)
            self.l_3_3 = QtWidgets.QLineEdit(Form)
            self.l_3_4 = QtWidgets.QLineEdit(Form)
            self.l_1_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_2_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_2_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_3.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_4.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_1_1.setGeometry(461, 37, 60, 20)
            self.l_2_1.setGeometry(194, 160, 60, 20)
            self.l_2_2.setGeometry(723, 160, 60, 20)
            self.l_3_1.setGeometry(139, 243, 60, 20)
            self.l_3_2.setGeometry(242, 243, 60, 20)
            self.l_3_3.setGeometry(676, 243, 60, 20)
            self.l_3_4.setGeometry(780, 243, 60, 20)

        if (self.size_x, self.size_y) == ('16', '64'):
            Form.setFixedSize(1240, 340)
            self.label.setGeometry(QtCore.QRect(0, 0, 1240, 280))
            self.pushButton1.setGeometry(QtCore.QRect(570, 293, 100, 30))
            self.label.setPixmap(QtGui.QPixmap("client\\resource\\upper\\16x64.png"))
            self.label.setAlignment(Qt.AlignCenter)

            self.l_1_1 = QtWidgets.QLineEdit(Form)
            self.l_2_1 = QtWidgets.QLineEdit(Form)
            self.l_2_2 = QtWidgets.QLineEdit(Form)
            self.l_3_1 = QtWidgets.QLineEdit(Form)
            self.l_3_2 = QtWidgets.QLineEdit(Form)
            self.l_3_3 = QtWidgets.QLineEdit(Form)
            self.l_3_4 = QtWidgets.QLineEdit(Form)
            self.l_4_1 = QtWidgets.QLineEdit(Form)
            self.l_4_2 = QtWidgets.QLineEdit(Form)
            self.l_4_3 = QtWidgets.QLineEdit(Form)
            self.l_4_4 = QtWidgets.QLineEdit(Form)
            self.l_4_5 = QtWidgets.QLineEdit(Form)
            self.l_4_6 = QtWidgets.QLineEdit(Form)
            self.l_4_7 = QtWidgets.QLineEdit(Form)
            self.l_4_8 = QtWidgets.QLineEdit(Form)
            self.l_1_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_2_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_2_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_3.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_4.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_3.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_4.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_5.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_6.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_7.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_8.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_1_1.setGeometry(589, 10, 60, 20)
            self.l_2_1.setGeometry(278, 47, 60, 20)
            self.l_2_2.setGeometry(903, 47, 60, 20)
            self.l_3_1.setGeometry(112, 118, 60, 20)
            self.l_3_2.setGeometry(444, 118, 60, 20)
            self.l_3_3.setGeometry(737, 118, 60, 20)
            self.l_3_4.setGeometry(1067, 118, 60, 20)
            self.l_4_1.setGeometry(86, 176, 50, 18)
            self.l_4_2.setGeometry(149, 176, 50, 18)
            self.l_4_3.setGeometry(417, 176, 50, 18)
            self.l_4_4.setGeometry(484, 176, 50, 18)
            self.l_4_5.setGeometry(710, 176, 50, 18)
            self.l_4_6.setGeometry(774, 176, 50, 18)
            self.l_4_7.setGeometry(1042, 176, 50, 18)
            self.l_4_8.setGeometry(1109, 176, 50, 18)

        if (self.size_x, self.size_y) == ('32', '32'):
            Form.setFixedSize(950, 700)
            self.label.setGeometry(QtCore.QRect(0, 0, 950, 650))
            self.pushButton1.setGeometry(QtCore.QRect(423, 658, 100, 30))
            self.label.setPixmap(QtGui.QPixmap("client\\resource\\upper\\32x32.png"))
            self.label.setAlignment(Qt.AlignCenter)

            self.l_1_1 = QtWidgets.QLineEdit(Form)
            self.l_2_1 = QtWidgets.QLineEdit(Form)
            self.l_2_2 = QtWidgets.QLineEdit(Form)
            self.l_3_1 = QtWidgets.QLineEdit(Form)
            self.l_3_2 = QtWidgets.QLineEdit(Form)
            self.l_3_3 = QtWidgets.QLineEdit(Form)
            self.l_3_4 = QtWidgets.QLineEdit(Form)
            self.l_4_1 = QtWidgets.QLineEdit(Form)
            self.l_4_2 = QtWidgets.QLineEdit(Form)
            self.l_4_3 = QtWidgets.QLineEdit(Form)
            self.l_4_4 = QtWidgets.QLineEdit(Form)
            self.l_4_5 = QtWidgets.QLineEdit(Form)
            self.l_4_6 = QtWidgets.QLineEdit(Form)
            self.l_4_7 = QtWidgets.QLineEdit(Form)
            self.l_4_8 = QtWidgets.QLineEdit(Form)
            self.l_1_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_2_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_2_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_3.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_4.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_3.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_4.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_5.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_6.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_7.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_8.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_1_1.setGeometry(444, 175, 60, 20)
            self.l_2_1.setGeometry(318, 345, 60, 20)
            self.l_2_2.setGeometry(583, 345, 60, 20)
            self.l_3_1.setGeometry(188, 252, 60, 20)
            self.l_3_2.setGeometry(707, 252, 60, 20)
            self.l_3_3.setGeometry(188, 427, 60, 20)
            self.l_3_4.setGeometry(707, 427, 60, 20)
            self.l_4_1.setGeometry(136, 178, 50, 20)
            self.l_4_2.setGeometry(239, 178, 50, 20)
            self.l_4_3.setGeometry(659, 178, 50, 20)
            self.l_4_4.setGeometry(759, 178, 50, 20)
            self.l_4_5.setGeometry(136, 519, 50, 20)
            self.l_4_6.setGeometry(239, 519, 50, 20)
            self.l_4_7.setGeometry(659, 519, 50, 20)
            self.l_4_8.setGeometry(759, 519, 50, 20)

        if (self.size_x, self.size_y) == ('32', '64'):
            Form.setFixedSize(1280, 600)
            self.label.setGeometry(QtCore.QRect(0, 0, 1280, 550))
            self.pushButton1.setGeometry(QtCore.QRect(589, 557, 100, 30))
            self.label.setPixmap(QtGui.QPixmap("client\\resource\\upper\\32x64.png"))
            self.label.setAlignment(Qt.AlignCenter)

            self.l_1_1 = QtWidgets.QLineEdit(Form)
            self.l_2_1 = QtWidgets.QLineEdit(Form)
            self.l_2_2 = QtWidgets.QLineEdit(Form)
            self.l_3_1 = QtWidgets.QLineEdit(Form)
            self.l_3_2 = QtWidgets.QLineEdit(Form)
            self.l_3_3 = QtWidgets.QLineEdit(Form)
            self.l_3_4 = QtWidgets.QLineEdit(Form)
            self.l_4_1 = QtWidgets.QLineEdit(Form)
            self.l_4_2 = QtWidgets.QLineEdit(Form)
            self.l_4_3 = QtWidgets.QLineEdit(Form)
            self.l_4_4 = QtWidgets.QLineEdit(Form)
            self.l_4_5 = QtWidgets.QLineEdit(Form)
            self.l_4_6 = QtWidgets.QLineEdit(Form)
            self.l_4_7 = QtWidgets.QLineEdit(Form)
            self.l_4_8 = QtWidgets.QLineEdit(Form)
            self.l_5_1 = QtWidgets.QLineEdit(Form)
            self.l_5_2 = QtWidgets.QLineEdit(Form)
            self.l_5_3 = QtWidgets.QLineEdit(Form)
            self.l_5_4 = QtWidgets.QLineEdit(Form)
            self.l_5_5 = QtWidgets.QLineEdit(Form)
            self.l_5_6 = QtWidgets.QLineEdit(Form)
            self.l_5_7 = QtWidgets.QLineEdit(Form)
            self.l_5_8 = QtWidgets.QLineEdit(Form)
            self.l_5_9 = QtWidgets.QLineEdit(Form)
            self.l_5_10 = QtWidgets.QLineEdit(Form)
            self.l_5_11 = QtWidgets.QLineEdit(Form)
            self.l_5_12 = QtWidgets.QLineEdit(Form)
            self.l_5_13 = QtWidgets.QLineEdit(Form)
            self.l_5_14 = QtWidgets.QLineEdit(Form)
            self.l_5_15 = QtWidgets.QLineEdit(Form)
            self.l_5_16 = QtWidgets.QLineEdit(Form)
            self.l_1_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_2_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_2_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_3.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_4.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_3.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_4.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_5.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_6.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_7.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_8.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_3.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_4.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_5.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_6.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_7.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_8.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_9.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_10.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_11.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_12.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_13.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_14.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_15.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_16.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_1_1.setGeometry(615, 32, 50, 20)
            self.l_2_1.setGeometry(295, 199, 50, 20)
            self.l_2_2.setGeometry(935, 199, 50, 20)
            self.l_3_1.setGeometry(210, 322, 50, 20)
            self.l_3_2.setGeometry(385, 322, 50, 20)
            self.l_3_3.setGeometry(853, 322, 50, 20)
            self.l_3_4.setGeometry(1025, 322, 50, 20)
            self.l_4_1.setGeometry(125, 254, 50, 20)
            self.l_4_2.setGeometry(465, 254, 50, 20)
            self.l_4_3.setGeometry(767, 254, 50, 20)
            self.l_4_4.setGeometry(1110, 254, 50, 20)
            self.l_4_5.setGeometry(125, 384, 50, 20)
            self.l_4_6.setGeometry(465, 384, 50, 20)
            self.l_4_7.setGeometry(767, 384, 50, 20)
            self.l_4_8.setGeometry(1110, 384, 50, 20)
            self.l_5_1.setGeometry(90, 198, 50, 20)
            self.l_5_2.setGeometry(157, 198, 50, 20)
            self.l_5_3.setGeometry(432, 198, 50, 20)
            self.l_5_4.setGeometry(498, 198, 50, 20)
            self.l_5_5.setGeometry(735, 198, 50, 20)
            self.l_5_6.setGeometry(802, 198, 50, 20)
            self.l_5_7.setGeometry(1080, 198, 50, 20)
            self.l_5_8.setGeometry(1145, 198, 50, 20)
            self.l_5_9.setGeometry(90, 447, 50, 20)
            self.l_5_10.setGeometry(157, 447, 50, 20)
            self.l_5_11.setGeometry(432, 447, 50, 20)
            self.l_5_12.setGeometry(498, 447, 50, 20)
            self.l_5_13.setGeometry(735, 447, 50, 20)
            self.l_5_14.setGeometry(802, 447, 50, 20)
            self.l_5_15.setGeometry(1080, 447, 50, 20)
            self.l_5_16.setGeometry(1145, 447, 50, 20)

        if (self.size_x, self.size_y) == ('64', '64'):
            Form.setFixedSize(1270, 1010)
            self.label.setGeometry(QtCore.QRect(0, 0, 1270, 970))
            self.pushButton1.setGeometry(QtCore.QRect(586, 950, 100, 30))
            self.label.setPixmap(QtGui.QPixmap("client\\resource\\upper\\64x64.png"))
            self.label.setAlignment(Qt.AlignCenter)

            self.l_1_1 = QtWidgets.QLineEdit(Form)
            self.l_2_1 = QtWidgets.QLineEdit(Form)
            self.l_2_2 = QtWidgets.QLineEdit(Form)
            self.l_3_1 = QtWidgets.QLineEdit(Form)
            self.l_3_2 = QtWidgets.QLineEdit(Form)
            self.l_3_3 = QtWidgets.QLineEdit(Form)
            self.l_3_4 = QtWidgets.QLineEdit(Form)
            self.l_4_1 = QtWidgets.QLineEdit(Form)
            self.l_4_2 = QtWidgets.QLineEdit(Form)
            self.l_4_3 = QtWidgets.QLineEdit(Form)
            self.l_4_4 = QtWidgets.QLineEdit(Form)
            self.l_4_5 = QtWidgets.QLineEdit(Form)
            self.l_4_6 = QtWidgets.QLineEdit(Form)
            self.l_4_7 = QtWidgets.QLineEdit(Form)
            self.l_4_8 = QtWidgets.QLineEdit(Form)
            self.l_5_1 = QtWidgets.QLineEdit(Form)
            self.l_5_2 = QtWidgets.QLineEdit(Form)
            self.l_5_3 = QtWidgets.QLineEdit(Form)
            self.l_5_4 = QtWidgets.QLineEdit(Form)
            self.l_5_5 = QtWidgets.QLineEdit(Form)
            self.l_5_6 = QtWidgets.QLineEdit(Form)
            self.l_5_7 = QtWidgets.QLineEdit(Form)
            self.l_5_8 = QtWidgets.QLineEdit(Form)
            self.l_5_9 = QtWidgets.QLineEdit(Form)
            self.l_5_10 = QtWidgets.QLineEdit(Form)
            self.l_5_11 = QtWidgets.QLineEdit(Form)
            self.l_5_12 = QtWidgets.QLineEdit(Form)
            self.l_5_13 = QtWidgets.QLineEdit(Form)
            self.l_5_14 = QtWidgets.QLineEdit(Form)
            self.l_5_15 = QtWidgets.QLineEdit(Form)
            self.l_5_16 = QtWidgets.QLineEdit(Form)
            self.l_6_1 = QtWidgets.QLineEdit(Form)
            self.l_6_2 = QtWidgets.QLineEdit(Form)
            self.l_6_3 = QtWidgets.QLineEdit(Form)
            self.l_6_4 = QtWidgets.QLineEdit(Form)
            self.l_6_5 = QtWidgets.QLineEdit(Form)
            self.l_6_6 = QtWidgets.QLineEdit(Form)
            self.l_6_7 = QtWidgets.QLineEdit(Form)
            self.l_6_8 = QtWidgets.QLineEdit(Form)
            self.l_6_9 = QtWidgets.QLineEdit(Form)
            self.l_6_10 = QtWidgets.QLineEdit(Form)
            self.l_6_11 = QtWidgets.QLineEdit(Form)
            self.l_6_12 = QtWidgets.QLineEdit(Form)
            self.l_6_13 = QtWidgets.QLineEdit(Form)
            self.l_6_14 = QtWidgets.QLineEdit(Form)
            self.l_6_15 = QtWidgets.QLineEdit(Form)
            self.l_6_16 = QtWidgets.QLineEdit(Form)
            self.l_6_17 = QtWidgets.QLineEdit(Form)
            self.l_6_18 = QtWidgets.QLineEdit(Form)
            self.l_6_19 = QtWidgets.QLineEdit(Form)
            self.l_6_20 = QtWidgets.QLineEdit(Form)
            self.l_6_21 = QtWidgets.QLineEdit(Form)
            self.l_6_22 = QtWidgets.QLineEdit(Form)
            self.l_6_23 = QtWidgets.QLineEdit(Form)
            self.l_6_24 = QtWidgets.QLineEdit(Form)
            self.l_6_25 = QtWidgets.QLineEdit(Form)
            self.l_6_26 = QtWidgets.QLineEdit(Form)
            self.l_6_27 = QtWidgets.QLineEdit(Form)
            self.l_6_28 = QtWidgets.QLineEdit(Form)
            self.l_6_29 = QtWidgets.QLineEdit(Form)
            self.l_6_30 = QtWidgets.QLineEdit(Form)
            self.l_6_31 = QtWidgets.QLineEdit(Form)
            self.l_6_32 = QtWidgets.QLineEdit(Form)
            self.l_1_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_2_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_2_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_3.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_3_4.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_3.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_4.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_5.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_6.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_7.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_4_8.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_3.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_4.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_5.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_6.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_7.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_8.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_9.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_10.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_11.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_12.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_13.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_14.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_15.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_5_16.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_1.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_2.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_3.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_4.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_5.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_6.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_7.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_8.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_9.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_10.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_11.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_12.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_13.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_14.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_15.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_16.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_17.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_18.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_19.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_20.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_21.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_22.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_23.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_24.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_25.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_26.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_27.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_28.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_29.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_30.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_31.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_6_32.setStyleSheet(
                "background-color:rgba(109, 109, 109, 40);border-width:0;border-style:outset;color:red")
            self.l_1_1.setGeometry(610, 259, 50, 20)
            self.l_2_1.setGeometry(440, 490, 50, 20)
            self.l_2_2.setGeometry(778, 490, 50, 20)
            self.l_3_1.setGeometry(280, 377, 50, 20)
            self.l_3_2.setGeometry(944, 377, 50, 20)
            self.l_3_3.setGeometry(280, 604, 50, 20)
            self.l_3_4.setGeometry(944, 604, 50, 20)
            self.l_4_1.setGeometry(200, 259, 50, 20)
            self.l_4_2.setGeometry(363, 259, 50, 20)
            self.l_4_3.setGeometry(861, 259, 50, 20)
            self.l_4_4.setGeometry(1022, 259, 50, 20)
            self.l_4_5.setGeometry(200, 723, 50, 20)
            self.l_4_6.setGeometry(363, 723, 50, 20)
            self.l_4_7.setGeometry(861, 723, 50, 20)
            self.l_4_8.setGeometry(1022, 723, 50, 20)
            self.l_5_1.setGeometry(112, 197, 50, 20)
            self.l_5_2.setGeometry(440, 197, 50, 20)
            self.l_5_3.setGeometry(778, 197, 50, 20)
            self.l_5_4.setGeometry(1106, 197, 50, 20)
            self.l_5_5.setGeometry(112, 316, 50, 20)
            self.l_5_6.setGeometry(440, 316, 50, 20)
            self.l_5_7.setGeometry(778, 316, 50, 20)
            self.l_5_8.setGeometry(1106, 316, 50, 20)
            self.l_5_9.setGeometry(112, 658, 50, 20)
            self.l_5_10.setGeometry(440, 658, 50, 20)
            self.l_5_11.setGeometry(778, 658, 50, 20)
            self.l_5_12.setGeometry(1106, 658, 50, 20)
            self.l_5_13.setGeometry(112, 784, 50, 20)
            self.l_5_14.setGeometry(440, 784, 50, 20)
            self.l_5_15.setGeometry(778, 784, 50, 20)
            self.l_5_16.setGeometry(1106, 784, 50, 20)
            self.l_6_1.setGeometry(82, 139, 50, 20)
            self.l_6_2.setGeometry(148, 139, 50, 20)
            self.l_6_3.setGeometry(410, 139, 50, 20)
            self.l_6_4.setGeometry(475, 139, 50, 20)
            self.l_6_5.setGeometry(747, 139, 50, 20)
            self.l_6_6.setGeometry(812, 139, 50, 20)
            self.l_6_7.setGeometry(1073, 139, 50, 20)
            self.l_6_8.setGeometry(1140, 139, 50, 20)
            self.l_6_9.setGeometry(82, 377, 50, 20)
            self.l_6_10.setGeometry(148, 377, 50, 20)
            self.l_6_11.setGeometry(410, 377, 50, 20)
            self.l_6_12.setGeometry(475, 377, 50, 20)
            self.l_6_13.setGeometry(747, 377, 50, 20)
            self.l_6_14.setGeometry(812, 377, 50, 20)
            self.l_6_15.setGeometry(1073, 377, 50, 20)
            self.l_6_16.setGeometry(1140, 377, 50, 20)
            self.l_6_17.setGeometry(85, 602, 50, 20)
            self.l_6_18.setGeometry(148, 602, 50, 20)
            self.l_6_19.setGeometry(410, 602, 50, 20)
            self.l_6_20.setGeometry(475, 602, 50, 20)
            self.l_6_21.setGeometry(747, 602, 50, 20)
            self.l_6_22.setGeometry(812, 602, 50, 20)
            self.l_6_23.setGeometry(1073, 602, 50, 20)
            self.l_6_24.setGeometry(1140, 602, 50, 20)
            self.l_6_25.setGeometry(85, 840, 50, 20)
            self.l_6_26.setGeometry(148, 840, 50, 20)
            self.l_6_27.setGeometry(410, 840, 50, 20)
            self.l_6_28.setGeometry(475, 840, 50, 20)
            self.l_6_29.setGeometry(747, 840, 50, 20)
            self.l_6_30.setGeometry(812, 840, 50, 20)
            self.l_6_31.setGeometry(1073, 840, 50, 20)
            self.l_6_32.setGeometry(1140, 840, 50, 20)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton1.setText(_translate("Form", "生成全部矩阵"))

    def confirm_input(self):
        self.subWin = Sub_MatrixForm()
        self.subExc = QtWidgets.QWidget()
        self.subWin.setupUi(self.subExc, (self.size_x, self.size_y))
        self.subWin.retranslateUi(self.subExc)
        self.subExc.show()






