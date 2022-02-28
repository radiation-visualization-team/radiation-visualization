import os
import numpy as np
import matplotlib.pyplot as plt


def draw2():
    a = np.array([0, 1, 2, 3])
    b = np.array([0, 1, 2, 3])
    plt.plot(a, b)
    figure_save_dir = "buffer"
    if not os.path.exists(figure_save_dir):
        os.makedirs(figure_save_dir)  # 如果不存在目录figure_save_path，则创建
    plt.savefig(os.path.join(figure_save_dir , 'draw2.png'))
