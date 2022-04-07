
def array_diagram(x, y):
    _size = [('8', '8'), ('8', '16'), ('8', '32'), ('16', '16'), ('16', '32'), ('16', '64'), ('32', '32'), ('32', '64'),
             ('64', '64')]
    if (x, y) not in _size:
        return

    figure_save_dir = "client\\resource\\{}x{}.png".format(x, y)
    # 画出
    return figure_save_dir


if __name__ == '__main__':
    array_diagram()
