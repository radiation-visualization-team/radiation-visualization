from PyQt5 import QtWidgets


def check_init(check):
    if check == False:
        QtWidgets.QMessageBox.information(None, '操作失败', '未设置参数')
        return True
    else:
        return False

def check_password(username, password):
    if username == 'admin' and password == '123456':
        return True
    else:
        QtWidgets.QMessageBox.information(None, '登录失败', '用户名或密码错误')
        return False
