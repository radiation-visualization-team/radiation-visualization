from PyQt5 import QtWidgets


def check_init(check):
    if check == False:
        QtWidgets.QMessageBox.information(None, '操作失败', '未设置参数')
        return True
    else:
        return False
