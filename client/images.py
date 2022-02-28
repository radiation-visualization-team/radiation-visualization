'''
这个模块用于为main.py准备5个可以放在MainWindow上的canvas，为此需要从draw模块拿到运算结果，给每一张图写一个用于画图的槽函数
https://blog.csdn.net/u013523007/article/details/89341724
'''
import os

from PyQt5.QtGui import QPixmap
from draw.darw_image1 import *
from draw.darw_image2 import *
from draw.darw_image3 import *
from draw.darw_image4 import *
from draw.darw_image5 import *
from utils.messabe_box import *


def draw_figure1(label, init):
    if check_init(init.stat): return
    figure_save_img = "buffer\\draw1.png"
    show_img = QPixmap(figure_save_img)
    if os.path.exists(figure_save_img):
        label.setPixmap(show_img)
    else:
        draw1()
        label.setPixmap(show_img)


def draw_figure2(label, init):
    if check_init(init.stat): return
    figure_save_img = "buffer\\draw2.png"
    show_img = QPixmap(figure_save_img)
    if os.path.exists(figure_save_img):
        label.setPixmap(show_img)
    else:
        draw2()
        label.setPixmap(show_img)


def draw_figure3(label, init):
    if check_init(init.stat): return
    figure_save_img = "buffer\\draw3.png"
    show_img = QPixmap(figure_save_img)
    if os.path.exists(figure_save_img):
        label.setPixmap(show_img)
    else:
        draw3()
        label.setPixmap(show_img)


def draw_figure4(label, init):
    if check_init(init.stat): return
    figure_save_img = "buffer\\draw4.png"
    show_img = QPixmap(figure_save_img)
    if os.path.exists(figure_save_img):
        label.setPixmap(show_img)
    else:
        draw4()
        label.setPixmap(show_img)


def draw_figure5(label, init):
    if check_init(init.stat): return
    figure_save_img = "buffer\\draw5.png"
    show_img = QPixmap(figure_save_img)
    if os.path.exists(figure_save_img):
        label.setPixmap(show_img)
    else:
        draw5()
        label.setPixmap(show_img)


def draw_all():
    draw1()
    draw2()
    draw3()
    draw4()
    draw5()
