from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from utils.computation import Graph, Graph_128


# 调试坐标临时用的label
class Templabel(QtWidgets.QLabel):

    # 调试用
    def mousePressEvent(self, event: QtGui.QMouseEvent):
        s = event.pos()
        self.setMouseTracking(True)
        self.click_x = s.x()
        self.click_y = s.y()
        print(f"x:{self.click_x} y:{self.click_y}")


class Array_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(760, 850)
        Form.setStyleSheet("background-color:white")
        # self.label = QtWidgets.QLabel(Form)
        self.label = Templabel(Form)
        # 暂时允许鼠标追踪
        self.label.setMouseTracking(True)

        self.label.setGeometry(QtCore.QRect(0, 10, 760, 780))
        self.label.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(325, 800, 100, 30))
        self.pushButton1.setObjectName("pushButton1")

        # 固定将天线阵列图居中放置
        self.label.setPixmap(QtGui.QPixmap("client\\resource\\aerial.jpg"))
        self.label.setAlignment(Qt.AlignCenter)

        # 初始化文本框
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
        self.l_7_1 = QtWidgets.QLineEdit(Form)
        self.l_7_2 = QtWidgets.QLineEdit(Form)
        self.l_7_3 = QtWidgets.QLineEdit(Form)
        self.l_7_4 = QtWidgets.QLineEdit(Form)
        self.l_7_5 = QtWidgets.QLineEdit(Form)
        self.l_7_6 = QtWidgets.QLineEdit(Form)
        self.l_7_7 = QtWidgets.QLineEdit(Form)
        self.l_7_8 = QtWidgets.QLineEdit(Form)
        self.l_7_9 = QtWidgets.QLineEdit(Form)
        self.l_7_10 = QtWidgets.QLineEdit(Form)
        self.l_7_11 = QtWidgets.QLineEdit(Form)
        self.l_7_12 = QtWidgets.QLineEdit(Form)
        self.l_7_13 = QtWidgets.QLineEdit(Form)
        self.l_7_14 = QtWidgets.QLineEdit(Form)
        self.l_7_15 = QtWidgets.QLineEdit(Form)
        self.l_7_16 = QtWidgets.QLineEdit(Form)
        self.l_7_17 = QtWidgets.QLineEdit(Form)
        self.l_7_18 = QtWidgets.QLineEdit(Form)
        self.l_7_19 = QtWidgets.QLineEdit(Form)
        self.l_7_20 = QtWidgets.QLineEdit(Form)
        self.l_7_21 = QtWidgets.QLineEdit(Form)
        self.l_7_22 = QtWidgets.QLineEdit(Form)
        self.l_7_23 = QtWidgets.QLineEdit(Form)
        self.l_7_24 = QtWidgets.QLineEdit(Form)
        self.l_7_25 = QtWidgets.QLineEdit(Form)
        self.l_7_26 = QtWidgets.QLineEdit(Form)
        self.l_7_27 = QtWidgets.QLineEdit(Form)
        self.l_7_28 = QtWidgets.QLineEdit(Form)
        self.l_7_29 = QtWidgets.QLineEdit(Form)
        self.l_7_30 = QtWidgets.QLineEdit(Form)
        self.l_7_31 = QtWidgets.QLineEdit(Form)
        self.l_7_32 = QtWidgets.QLineEdit(Form)
        self.l_7_33 = QtWidgets.QLineEdit(Form)
        self.l_7_34 = QtWidgets.QLineEdit(Form)
        self.l_7_35 = QtWidgets.QLineEdit(Form)
        self.l_7_36 = QtWidgets.QLineEdit(Form)
        self.l_7_37 = QtWidgets.QLineEdit(Form)
        self.l_7_38 = QtWidgets.QLineEdit(Form)
        self.l_7_39 = QtWidgets.QLineEdit(Form)
        self.l_7_40 = QtWidgets.QLineEdit(Form)
        self.l_7_41 = QtWidgets.QLineEdit(Form)
        self.l_7_42 = QtWidgets.QLineEdit(Form)
        self.l_7_43 = QtWidgets.QLineEdit(Form)
        self.l_7_44 = QtWidgets.QLineEdit(Form)
        self.l_7_45 = QtWidgets.QLineEdit(Form)
        self.l_7_46 = QtWidgets.QLineEdit(Form)
        self.l_7_47 = QtWidgets.QLineEdit(Form)
        self.l_7_48 = QtWidgets.QLineEdit(Form)
        self.l_7_49 = QtWidgets.QLineEdit(Form)
        self.l_7_50 = QtWidgets.QLineEdit(Form)
        self.l_7_51 = QtWidgets.QLineEdit(Form)
        self.l_7_52 = QtWidgets.QLineEdit(Form)
        self.l_7_53 = QtWidgets.QLineEdit(Form)
        self.l_7_54 = QtWidgets.QLineEdit(Form)
        self.l_7_55 = QtWidgets.QLineEdit(Form)
        self.l_7_56 = QtWidgets.QLineEdit(Form)
        self.l_7_57 = QtWidgets.QLineEdit(Form)
        self.l_7_58 = QtWidgets.QLineEdit(Form)
        self.l_7_59 = QtWidgets.QLineEdit(Form)
        self.l_7_60 = QtWidgets.QLineEdit(Form)
        self.l_7_61 = QtWidgets.QLineEdit(Form)
        self.l_7_62 = QtWidgets.QLineEdit(Form)
        self.l_7_63 = QtWidgets.QLineEdit(Form)
        self.l_7_64 = QtWidgets.QLineEdit(Form)

        # 将全部文本框设置为同一个样式
        self.l_1_1.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_2_1.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_2_2.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_3_1.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_3_2.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_3_3.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_3_4.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_4_1.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_4_2.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_4_3.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_4_4.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_4_5.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_4_6.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_4_7.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_4_8.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_1.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_2.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_3.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_4.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_5.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_6.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_7.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_8.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_9.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_10.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_11.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_12.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_13.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_14.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_15.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_5_16.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_1.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_2.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_3.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_4.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_5.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_6.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_7.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_8.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_9.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_10.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_11.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_12.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_13.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_14.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_15.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_16.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_17.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_18.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_19.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_20.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_21.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_22.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_23.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_24.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_25.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_26.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_27.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_28.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_29.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_30.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_31.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_6_32.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_1.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_2.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_3.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_4.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_5.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_6.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_7.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_8.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_9.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_10.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_11.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_12.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_13.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_14.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_15.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_16.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_17.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_18.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_19.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_20.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_21.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_22.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_23.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_24.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_25.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_26.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_27.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_28.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_29.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_30.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_31.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_32.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_33.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_34.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_35.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_36.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_37.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_38.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_39.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_40.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_41.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_42.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_43.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_44.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_45.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_46.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_47.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_48.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_49.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_50.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_51.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_52.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_53.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_54.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_55.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_56.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_57.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_58.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_59.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_60.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_61.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_62.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_63.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")
        self.l_7_64.setStyleSheet(
            "background-color:rgba(109, 109, 109, 20);border-width:0;border-style:outset;color:red")

        # 设置文本框位置 1
        self.l_1_1.setGeometry(530, 390, 40, 20)

        # 设置文本框位置 2
        self.l_2_1.setGeometry(356, 309, 40, 20)
        self.l_2_2.setGeometry(356, 476, 40, 20)

        # # 设置文本框位置 4
        self.l_3_1.setGeometry(271, 198, 40, 20)
        self.l_3_2.setGeometry(438, 198, 40, 20)
        self.l_3_3.setGeometry(271, 583, 40, 20)
        self.l_3_4.setGeometry(438, 583, 40, 20)
        #
        # # 设置文本框位置 8
        self.l_4_1.setGeometry(191, 143, 40, 20)
        self.l_4_2.setGeometry(519, 143, 40, 20)
        self.l_4_3.setGeometry(191, 254, 40, 20)
        self.l_4_4.setGeometry(519, 254, 40, 20)
        self.l_4_5.setGeometry(191, 530, 40, 20)
        self.l_4_6.setGeometry(519, 530, 40, 20)
        self.l_4_7.setGeometry(191, 636, 40, 20)
        self.l_4_8.setGeometry(519, 636, 40, 20)
        #
        # # 设置文本框位置 16
        self.l_5_1.setGeometry(150, 91, 40, 20)
        self.l_5_2.setGeometry(235, 91, 40, 20)
        self.l_5_3.setGeometry(477, 91, 40, 20)
        self.l_5_4.setGeometry(562, 91, 40, 20)
        self.l_5_5.setGeometry(150, 308, 40, 20)
        self.l_5_6.setGeometry(235, 308, 40, 20)
        self.l_5_7.setGeometry(477, 308, 40, 20)
        self.l_5_8.setGeometry(562, 308, 40, 20)
        self.l_5_9.setGeometry(150, 473, 40, 20)
        self.l_5_10.setGeometry(235, 473, 40, 20)
        self.l_5_11.setGeometry(477, 473, 40, 20)
        self.l_5_12.setGeometry(562, 473, 40, 20)
        self.l_5_13.setGeometry(150, 693, 40, 20)
        self.l_5_14.setGeometry(235, 693, 40, 20)
        self.l_5_15.setGeometry(477, 693, 40, 20)
        self.l_5_16.setGeometry(562, 693, 40, 20)
        #
        # # 设置文本框位置 32
        self.l_6_1.setGeometry(105, 59, 40, 20)
        self.l_6_2.setGeometry(267, 59, 40, 20)
        self.l_6_3.setGeometry(433, 59, 40, 20)
        self.l_6_4.setGeometry(596, 59, 40, 20)
        self.l_6_5.setGeometry(105, 118, 40, 20)
        self.l_6_6.setGeometry(267, 118, 40, 20)
        self.l_6_7.setGeometry(433, 118, 40, 20)
        self.l_6_8.setGeometry(596, 118, 40, 20)
        self.l_6_9.setGeometry(105, 280, 40, 20)
        self.l_6_10.setGeometry(267, 280, 40, 20)
        self.l_6_11.setGeometry(433, 280, 40, 20)
        self.l_6_12.setGeometry(596, 280, 40, 20)
        self.l_6_13.setGeometry(105, 336, 40, 20)
        self.l_6_14.setGeometry(267, 336, 40, 20)
        self.l_6_15.setGeometry(433, 336, 40, 20)
        self.l_6_16.setGeometry(596, 336, 40, 20)
        self.l_6_17.setGeometry(105, 448, 40, 20)
        self.l_6_18.setGeometry(267, 448, 40, 20)
        self.l_6_19.setGeometry(433, 448, 40, 20)
        self.l_6_20.setGeometry(596, 448, 40, 20)
        self.l_6_21.setGeometry(105, 501, 40, 20)
        self.l_6_22.setGeometry(267, 501, 40, 20)
        self.l_6_23.setGeometry(433, 501, 40, 20)
        self.l_6_24.setGeometry(596, 501, 40, 20)
        self.l_6_25.setGeometry(105, 662, 40, 20)
        self.l_6_26.setGeometry(267, 662, 40, 20)
        self.l_6_27.setGeometry(433, 662, 40, 20)
        self.l_6_28.setGeometry(596, 662, 40, 20)
        self.l_6_29.setGeometry(105, 721, 40, 20)
        self.l_6_30.setGeometry(267, 721, 40, 20)
        self.l_6_31.setGeometry(433, 721, 40, 20)
        self.l_6_32.setGeometry(596, 721, 40, 20)
        #
        # # 设置文本框位置 64
        self.l_7_1.setGeometry(77, 35, 40, 20)
        self.l_7_2.setGeometry(132, 35, 40, 20)
        self.l_7_3.setGeometry(240, 35, 40, 20)
        self.l_7_4.setGeometry(296, 35, 40, 20)
        self.l_7_5.setGeometry(404, 35, 40, 20)
        self.l_7_6.setGeometry(460, 35, 40, 20)
        self.l_7_7.setGeometry(569, 35, 40, 20)
        self.l_7_8.setGeometry(625, 35, 40, 20)
        self.l_7_9.setGeometry(77, 145, 40, 20)
        self.l_7_10.setGeometry(132, 145, 40, 20)
        self.l_7_11.setGeometry(240, 145, 40, 20)
        self.l_7_12.setGeometry(296, 145, 40, 20)
        self.l_7_13.setGeometry(404, 145, 40, 20)
        self.l_7_14.setGeometry(460, 145, 40, 20)
        self.l_7_15.setGeometry(569, 145, 40, 20)
        self.l_7_16.setGeometry(625, 145, 40, 20)
        self.l_7_17.setGeometry(77, 253, 40, 20)
        self.l_7_18.setGeometry(132, 253, 40, 20)
        self.l_7_19.setGeometry(240, 253, 40, 20)
        self.l_7_20.setGeometry(296, 253, 40, 20)
        self.l_7_21.setGeometry(404, 253, 40, 20)
        self.l_7_22.setGeometry(460, 253, 40, 20)
        self.l_7_23.setGeometry(569, 253, 40, 20)
        self.l_7_24.setGeometry(625, 253, 40, 20)
        self.l_7_25.setGeometry(77, 363, 40, 20)
        self.l_7_26.setGeometry(132, 363, 40, 20)
        self.l_7_27.setGeometry(240, 363, 40, 20)
        self.l_7_28.setGeometry(296, 363, 40, 20)
        self.l_7_29.setGeometry(404, 363, 40, 20)
        self.l_7_30.setGeometry(460, 363, 40, 20)
        self.l_7_31.setGeometry(569, 363, 40, 20)
        self.l_7_32.setGeometry(625, 363, 40, 20)
        self.l_7_33.setGeometry(77, 419, 40, 20)
        self.l_7_34.setGeometry(132, 419, 40, 20)
        self.l_7_35.setGeometry(240, 419, 40, 20)
        self.l_7_36.setGeometry(296, 419, 40, 20)
        self.l_7_37.setGeometry(404, 419, 40, 20)
        self.l_7_38.setGeometry(460, 419, 40, 20)
        self.l_7_39.setGeometry(569, 419, 40, 20)
        self.l_7_40.setGeometry(625, 419, 40, 20)
        self.l_7_41.setGeometry(77, 529, 40, 20)
        self.l_7_42.setGeometry(132, 529, 40, 20)
        self.l_7_43.setGeometry(240, 529, 40, 20)
        self.l_7_44.setGeometry(296, 529, 40, 20)
        self.l_7_45.setGeometry(404, 529, 40, 20)
        self.l_7_46.setGeometry(460, 529, 40, 20)
        self.l_7_47.setGeometry(569, 529, 40, 20)
        self.l_7_48.setGeometry(625, 529, 40, 20)
        self.l_7_49.setGeometry(77, 637, 40, 20)
        self.l_7_50.setGeometry(132, 637, 40, 20)
        self.l_7_51.setGeometry(240, 637, 40, 20)
        self.l_7_52.setGeometry(296, 637, 40, 20)
        self.l_7_53.setGeometry(407, 637, 40, 20)
        self.l_7_54.setGeometry(463, 637, 40, 20)
        self.l_7_55.setGeometry(569, 637, 40, 20)
        self.l_7_56.setGeometry(625, 637, 40, 20)
        self.l_7_57.setGeometry(77, 746, 40, 20)
        self.l_7_58.setGeometry(132, 746, 40, 20)
        self.l_7_59.setGeometry(240, 746, 40, 20)
        self.l_7_60.setGeometry(296, 746, 40, 20)
        self.l_7_61.setGeometry(407, 746, 40, 20)
        self.l_7_62.setGeometry(463, 746, 40, 20)
        self.l_7_63.setGeometry(569, 746, 40, 20)
        self.l_7_64.setGeometry(625, 746, 40, 20)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton1.setText(_translate("Form", "查看生成矩阵"))

    def confirm_input(self):
        self.text1 = self.l_1_1.text()
        self.text2 = self.l_2_1.text()
        self.text3 = self.l_2_2.text()
        self.text4 = self.l_3_1.text()
        self.text5 = self.l_3_2.text()
        self.text6 = self.l_3_3.text()
        self.text7 = self.l_3_4.text()
        self.text8 = self.l_4_1.text()
        self.text9 = self.l_4_2.text()
        self.text10 = self.l_4_3.text()
        self.text11 = self.l_4_4.text()
        self.text12 = self.l_4_5.text()
        self.text13 = self.l_4_6.text()
        self.text14 = self.l_4_7.text()
        self.text15 = self.l_4_8.text()
        self.text16 = self.l_5_1.text()
        self.text17 = self.l_5_2.text()
        self.text18 = self.l_5_3.text()
        self.text19 = self.l_5_4.text()
        self.text20 = self.l_5_5.text()
        self.text21 = self.l_5_6.text()
        self.text22 = self.l_5_7.text()
        self.text23 = self.l_5_8.text()
        self.text24 = self.l_5_9.text()
        self.text25 = self.l_5_10.text()
        self.text26 = self.l_5_11.text()
        self.text27 = self.l_5_12.text()
        self.text28 = self.l_5_13.text()
        self.text29 = self.l_5_14.text()
        self.text30 = self.l_5_15.text()
        self.text31 = self.l_5_16.text()
        self.text32 = self.l_6_1.text()
        self.text33 = self.l_6_2.text()
        self.text34 = self.l_6_3.text()
        self.text35 = self.l_6_4.text()
        self.text36 = self.l_6_5.text()
        self.text37 = self.l_6_6.text()
        self.text38 = self.l_6_7.text()
        self.text39 = self.l_6_8.text()
        self.text40 = self.l_6_9.text()
        self.text41 = self.l_6_10.text()
        self.text42 = self.l_6_11.text()
        self.text43 = self.l_6_12.text()
        self.text44 = self.l_6_13.text()
        self.text45 = self.l_6_14.text()
        self.text46 = self.l_6_15.text()
        self.text47 = self.l_6_16.text()
        self.text48 = self.l_6_17.text()
        self.text49 = self.l_6_18.text()
        self.text50 = self.l_6_19.text()
        self.text51 = self.l_6_20.text()
        self.text52 = self.l_6_21.text()
        self.text53 = self.l_6_22.text()
        self.text54 = self.l_6_23.text()
        self.text55 = self.l_6_24.text()
        self.text56 = self.l_6_25.text()
        self.text57 = self.l_6_26.text()
        self.text58 = self.l_6_27.text()
        self.text59 = self.l_6_28.text()
        self.text60 = self.l_6_29.text()
        self.text61 = self.l_6_30.text()
        self.text62 = self.l_6_31.text()
        self.text63 = self.l_6_32.text()
        self.text64 = self.l_7_1.text()
        self.text65 = self.l_7_2.text()
        self.text66 = self.l_7_3.text()
        self.text67 = self.l_7_4.text()
        self.text68 = self.l_7_5.text()
        self.text69 = self.l_7_6.text()
        self.text70 = self.l_7_7.text()
        self.text71 = self.l_7_8.text()
        self.text72 = self.l_7_9.text()
        self.text73 = self.l_7_10.text()
        self.text74 = self.l_7_11.text()
        self.text75 = self.l_7_12.text()
        self.text76 = self.l_7_13.text()
        self.text77 = self.l_7_14.text()
        self.text78 = self.l_7_15.text()
        self.text79 = self.l_7_16.text()
        self.text80 = self.l_7_17.text()
        self.text81 = self.l_7_18.text()
        self.text82 = self.l_7_19.text()
        self.text83 = self.l_7_20.text()
        self.text84 = self.l_7_21.text()
        self.text85 = self.l_7_22.text()
        self.text86 = self.l_7_23.text()
        self.text87 = self.l_7_24.text()
        self.text88 = self.l_7_25.text()
        self.text89 = self.l_7_26.text()
        self.text90 = self.l_7_27.text()
        self.text91 = self.l_7_28.text()
        self.text92 = self.l_7_29.text()
        self.text93 = self.l_7_30.text()
        self.text94 = self.l_7_31.text()
        self.text95 = self.l_7_32.text()
        self.text96 = self.l_7_33.text()
        self.text97 = self.l_7_34.text()
        self.text98 = self.l_7_35.text()
        self.text99 = self.l_7_36.text()
        self.text100 = self.l_7_37.text()
        self.text101 = self.l_7_38.text()
        self.text102 = self.l_7_39.text()
        self.text103 = self.l_7_40.text()
        self.text104 = self.l_7_41.text()
        self.text105 = self.l_7_42.text()
        self.text106 = self.l_7_43.text()
        self.text107 = self.l_7_44.text()
        self.text108 = self.l_7_45.text()
        self.text109 = self.l_7_46.text()
        self.text110 = self.l_7_47.text()
        self.text111 = self.l_7_48.text()
        self.text112 = self.l_7_49.text()
        self.text113 = self.l_7_50.text()
        self.text114 = self.l_7_51.text()
        self.text115 = self.l_7_52.text()
        self.text116 = self.l_7_53.text()
        self.text117 = self.l_7_54.text()
        self.text118 = self.l_7_55.text()
        self.text119 = self.l_7_56.text()
        self.text120 = self.l_7_57.text()
        self.text121 = self.l_7_58.text()
        self.text122 = self.l_7_59.text()
        self.text123 = self.l_7_60.text()
        self.text124 = self.l_7_61.text()
        self.text125 = self.l_7_62.text()
        self.text126 = self.l_7_63.text()
        self.text127 = self.l_7_64.text()

        self.l_1_1.setText(self.text1)
        self.l_2_1.setText(self.text2)
        self.l_2_2.setText(self.text3)
        self.l_3_1.setText(self.text4)
        self.l_3_2.setText(self.text5)
        self.l_3_3.setText(self.text6)
        self.l_3_4.setText(self.text7)
        self.l_4_1.setText(self.text8)
        self.l_4_2.setText(self.text9)
        self.l_4_3.setText(self.text10)
        self.l_4_4.setText(self.text11)
        self.l_4_5.setText(self.text12)
        self.l_4_6.setText(self.text13)
        self.l_4_7.setText(self.text14)
        self.l_4_8.setText(self.text15)
        self.l_5_1.setText(self.text16)
        self.l_5_2.setText(self.text17)
        self.l_5_3.setText(self.text18)
        self.l_5_4.setText(self.text19)
        self.l_5_5.setText(self.text20)
        self.l_5_6.setText(self.text21)
        self.l_5_7.setText(self.text22)
        self.l_5_8.setText(self.text23)
        self.l_5_9.setText(self.text24)
        self.l_5_10.setText(self.text25)
        self.l_5_11.setText(self.text26)
        self.l_5_12.setText(self.text27)
        self.l_5_13.setText(self.text28)
        self.l_5_14.setText(self.text29)
        self.l_5_15.setText(self.text30)
        self.l_5_16.setText(self.text31)
        self.l_6_1.setText(self.text32)
        self.l_6_2.setText(self.text33)
        self.l_6_3.setText(self.text34)
        self.l_6_4.setText(self.text35)
        self.l_6_5.setText(self.text36)
        self.l_6_6.setText(self.text37)
        self.l_6_7.setText(self.text38)
        self.l_6_8.setText(self.text39)
        self.l_6_9.setText(self.text40)
        self.l_6_10.setText(self.text41)
        self.l_6_11.setText(self.text42)
        self.l_6_12.setText(self.text43)
        self.l_6_13.setText(self.text44)
        self.l_6_14.setText(self.text45)
        self.l_6_15.setText(self.text46)
        self.l_6_16.setText(self.text47)
        self.l_6_17.setText(self.text48)
        self.l_6_18.setText(self.text49)
        self.l_6_19.setText(self.text50)
        self.l_6_20.setText(self.text51)
        self.l_6_21.setText(self.text52)
        self.l_6_22.setText(self.text53)
        self.l_6_23.setText(self.text54)
        self.l_6_24.setText(self.text55)
        self.l_6_25.setText(self.text56)
        self.l_6_26.setText(self.text57)
        self.l_6_27.setText(self.text58)
        self.l_6_28.setText(self.text59)
        self.l_6_29.setText(self.text60)
        self.l_6_30.setText(self.text61)
        self.l_6_31.setText(self.text62)
        self.l_6_32.setText(self.text63)
        self.l_7_1.setText(self.text64)
        self.l_7_2.setText(self.text65)
        self.l_7_3.setText(self.text66)
        self.l_7_4.setText(self.text67)
        self.l_7_5.setText(self.text68)
        self.l_7_6.setText(self.text69)
        self.l_7_7.setText(self.text70)
        self.l_7_8.setText(self.text71)
        self.l_7_9.setText(self.text72)
        self.l_7_10.setText(self.text73)
        self.l_7_11.setText(self.text74)
        self.l_7_12.setText(self.text75)
        self.l_7_13.setText(self.text76)
        self.l_7_14.setText(self.text77)
        self.l_7_15.setText(self.text78)
        self.l_7_16.setText(self.text79)
        self.l_7_17.setText(self.text80)
        self.l_7_18.setText(self.text81)
        self.l_7_19.setText(self.text82)
        self.l_7_20.setText(self.text83)
        self.l_7_21.setText(self.text84)
        self.l_7_22.setText(self.text85)
        self.l_7_23.setText(self.text86)
        self.l_7_24.setText(self.text87)
        self.l_7_25.setText(self.text88)
        self.l_7_26.setText(self.text89)
        self.l_7_27.setText(self.text90)
        self.l_7_28.setText(self.text91)
        self.l_7_29.setText(self.text92)
        self.l_7_30.setText(self.text93)
        self.l_7_31.setText(self.text94)
        self.l_7_32.setText(self.text95)
        self.l_7_33.setText(self.text96)
        self.l_7_34.setText(self.text97)
        self.l_7_35.setText(self.text98)
        self.l_7_36.setText(self.text99)
        self.l_7_37.setText(self.text100)
        self.l_7_38.setText(self.text101)
        self.l_7_39.setText(self.text102)
        self.l_7_40.setText(self.text103)
        self.l_7_41.setText(self.text104)
        self.l_7_42.setText(self.text105)
        self.l_7_43.setText(self.text106)
        self.l_7_44.setText(self.text107)
        self.l_7_45.setText(self.text108)
        self.l_7_46.setText(self.text109)
        self.l_7_47.setText(self.text110)
        self.l_7_48.setText(self.text111)
        self.l_7_49.setText(self.text112)
        self.l_7_50.setText(self.text113)
        self.l_7_51.setText(self.text114)
        self.l_7_52.setText(self.text115)
        self.l_7_53.setText(self.text116)
        self.l_7_54.setText(self.text117)
        self.l_7_55.setText(self.text118)
        self.l_7_56.setText(self.text119)
        self.l_7_57.setText(self.text120)
        self.l_7_58.setText(self.text121)
        self.l_7_59.setText(self.text122)
        self.l_7_60.setText(self.text123)
        self.l_7_61.setText(self.text124)
        self.l_7_62.setText(self.text125)
        self.l_7_63.setText(self.text126)
        self.l_7_64.setText(self.text127)

        QtWidgets.QMessageBox.information(None, "设置参数", "参数设置成功")

        self.mapping()

    def mapping(self):
        attributes = []

        attributes.append(float(self.text1) if self.text1 != '' else 0)
        attributes.append(float(self.text2) if self.text2 != '' else 0)
        attributes.append(float(self.text3) if self.text3 != '' else 0)
        attributes.append(float(self.text4) if self.text4 != '' else 0)
        attributes.append(float(self.text5) if self.text5 != '' else 0)
        attributes.append(float(self.text6) if self.text6 != '' else 0)
        attributes.append(float(self.text7) if self.text7 != '' else 0)
        attributes.append(float(self.text8) if self.text8 != '' else 0)
        attributes.append(float(self.text10) if self.text10 != '' else 0)
        attributes.append(float(self.text9) if self.text9 != '' else 0)
        attributes.append(float(self.text11) if self.text11 != '' else 0)
        attributes.append(float(self.text12) if self.text12 != '' else 0)
        attributes.append(float(self.text14) if self.text14 != '' else 0)
        attributes.append(float(self.text13) if self.text13 != '' else 0)
        attributes.append(float(self.text15) if self.text15 != '' else 0)
        attributes.append(float(self.text16) if self.text16 != '' else 0)
        attributes.append(float(self.text17) if self.text17 != '' else 0)
        attributes.append(float(self.text20) if self.text20 != '' else 0)
        attributes.append(float(self.text21) if self.text21 != '' else 0)
        attributes.append(float(self.text18) if self.text18 != '' else 0)
        attributes.append(float(self.text19) if self.text19 != '' else 0)
        attributes.append(float(self.text22) if self.text22 != '' else 0)
        attributes.append(float(self.text23) if self.text23 != '' else 0)
        attributes.append(float(self.text24) if self.text24 != '' else 0)
        attributes.append(float(self.text25) if self.text25 != '' else 0)
        attributes.append(float(self.text28) if self.text28 != '' else 0)
        attributes.append(float(self.text29) if self.text29 != '' else 0)
        attributes.append(float(self.text26) if self.text26 != '' else 0)
        attributes.append(float(self.text27) if self.text27 != '' else 0)
        attributes.append(float(self.text30) if self.text30 != '' else 0)
        attributes.append(float(self.text31) if self.text31 != '' else 0)
        attributes.append(float(self.text32) if self.text32 != '' else 0)
        attributes.append(float(self.text36) if self.text36 != '' else 0)
        attributes.append(float(self.text33) if self.text33 != '' else 0)
        attributes.append(float(self.text37) if self.text37 != '' else 0)
        attributes.append(float(self.text40) if self.text40 != '' else 0)
        attributes.append(float(self.text44) if self.text44 != '' else 0)
        attributes.append(float(self.text41) if self.text41 != '' else 0)
        attributes.append(float(self.text45) if self.text45 != '' else 0)
        attributes.append(float(self.text34) if self.text34 != '' else 0)
        attributes.append(float(self.text38) if self.text38 != '' else 0)
        attributes.append(float(self.text36) if self.text36 != '' else 0)
        attributes.append(float(self.text39) if self.text39 != '' else 0)
        attributes.append(float(self.text42) if self.text42 != '' else 0)
        attributes.append(float(self.text46) if self.text46 != '' else 0)
        attributes.append(float(self.text43) if self.text43 != '' else 0)
        attributes.append(float(self.text47) if self.text47 != '' else 0)
        attributes.append(float(self.text48) if self.text48 != '' else 0)
        attributes.append(float(self.text52) if self.text52 != '' else 0)
        attributes.append(float(self.text49) if self.text49 != '' else 0)
        attributes.append(float(self.text53) if self.text53 != '' else 0)
        attributes.append(float(self.text56) if self.text56 != '' else 0)
        attributes.append(float(self.text60) if self.text60 != '' else 0)
        attributes.append(float(self.text57) if self.text57 != '' else 0)
        attributes.append(float(self.text61) if self.text61 != '' else 0)
        attributes.append(float(self.text50) if self.text50 != '' else 0)
        attributes.append(float(self.text54) if self.text54 != '' else 0)
        attributes.append(float(self.text51) if self.text51 != '' else 0)
        attributes.append(float(self.text55) if self.text55 != '' else 0)
        attributes.append(float(self.text58) if self.text58 != '' else 0)
        attributes.append(float(self.text62) if self.text62 != '' else 0)
        attributes.append(float(self.text59) if self.text59 != '' else 0)
        attributes.append(float(self.text63) if self.text63 != '' else 0)
        attributes.append(float(self.text64) if self.text64 != '' else 0)
        attributes.append(float(self.text65) if self.text65 != '' else 0)
        attributes.append(float(self.text72) if self.text72 != '' else 0)
        attributes.append(float(self.text73) if self.text73 != '' else 0)
        attributes.append(float(self.text66) if self.text66 != '' else 0)
        attributes.append(float(self.text67) if self.text67 != '' else 0)
        attributes.append(float(self.text74) if self.text74 != '' else 0)
        attributes.append(float(self.text75) if self.text75 != '' else 0)
        attributes.append(float(self.text80) if self.text80 != '' else 0)
        attributes.append(float(self.text81) if self.text81 != '' else 0)
        attributes.append(float(self.text88) if self.text88 != '' else 0)
        attributes.append(float(self.text89) if self.text89 != '' else 0)
        attributes.append(float(self.text82) if self.text82 != '' else 0)
        attributes.append(float(self.text83) if self.text83 != '' else 0)
        attributes.append(float(self.text90) if self.text90 != '' else 0)
        attributes.append(float(self.text91) if self.text91 != '' else 0)
        attributes.append(float(self.text68) if self.text68 != '' else 0)
        attributes.append(float(self.text69) if self.text69 != '' else 0)
        attributes.append(float(self.text76) if self.text76 != '' else 0)
        attributes.append(float(self.text77) if self.text77 != '' else 0)
        attributes.append(float(self.text70) if self.text70 != '' else 0)
        attributes.append(float(self.text71) if self.text71 != '' else 0)
        attributes.append(float(self.text78) if self.text78 != '' else 0)
        attributes.append(float(self.text79) if self.text79 != '' else 0)
        attributes.append(float(self.text84) if self.text84 != '' else 0)
        attributes.append(float(self.text85) if self.text85 != '' else 0)
        attributes.append(float(self.text92) if self.text92 != '' else 0)
        attributes.append(float(self.text93) if self.text93 != '' else 0)
        attributes.append(float(self.text86) if self.text86 != '' else 0)
        attributes.append(float(self.text87) if self.text87 != '' else 0)
        attributes.append(float(self.text94) if self.text94 != '' else 0)
        attributes.append(float(self.text95) if self.text95 != '' else 0)
        attributes.append(float(self.text96) if self.text96 != '' else 0)
        attributes.append(float(self.text97) if self.text97 != '' else 0)
        attributes.append(float(self.text104) if self.text104 != '' else 0)
        attributes.append(float(self.text105) if self.text105 != '' else 0)
        attributes.append(float(self.text98) if self.text98 != '' else 0)
        attributes.append(float(self.text99) if self.text99 != '' else 0)
        attributes.append(float(self.text106) if self.text106 != '' else 0)
        attributes.append(float(self.text107) if self.text107 != '' else 0)
        attributes.append(float(self.text112) if self.text112 != '' else 0)
        attributes.append(float(self.text113) if self.text113 != '' else 0)
        attributes.append(float(self.text120) if self.text120 != '' else 0)
        attributes.append(float(self.text121) if self.text121 != '' else 0)
        attributes.append(float(self.text114) if self.text114 != '' else 0)
        attributes.append(float(self.text115) if self.text115 != '' else 0)
        attributes.append(float(self.text122) if self.text122 != '' else 0)
        attributes.append(float(self.text123) if self.text123 != '' else 0)
        attributes.append(float(self.text100) if self.text100 != '' else 0)
        attributes.append(float(self.text101) if self.text101 != '' else 0)
        attributes.append(float(self.text108) if self.text108 != '' else 0)
        attributes.append(float(self.text109) if self.text109 != '' else 0)
        attributes.append(float(self.text102) if self.text102 != '' else 0)
        attributes.append(float(self.text103) if self.text103 != '' else 0)
        attributes.append(float(self.text110) if self.text110 != '' else 0)
        attributes.append(float(self.text111) if self.text111 != '' else 0)
        attributes.append(float(self.text116) if self.text116 != '' else 0)
        attributes.append(float(self.text117) if self.text117 != '' else 0)
        attributes.append(float(self.text124) if self.text124 != '' else 0)
        attributes.append(float(self.text125) if self.text125 != '' else 0)
        attributes.append(float(self.text118) if self.text118 != '' else 0)
        attributes.append(float(self.text119) if self.text119 != '' else 0)
        attributes.append(float(self.text126) if self.text126 != '' else 0)
        attributes.append(float(self.text127) if self.text127 != '' else 0)

        g = Graph()
        graph_c = Graph_128(g, attributes)
        _ = graph_c.createGraph()
        matrix_a = graph_c.createMatrix()

        for v in _:
            print(v, v.total_weight)

        for _, i in enumerate(matrix_a):
            print("{}: {}".format(_, i))
























