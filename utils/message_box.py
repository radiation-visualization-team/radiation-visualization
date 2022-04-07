from PyQt5 import QtWidgets


# 如果无初始化，则弹出信息窗口
def check_init(check):
    if check == False:
        QtWidgets.QMessageBox.information(None, '操作失败', '未设置参数')
        return True
    else:
        return False


# 如果账号或密码错误，则弹出信息窗口
def check_password(username, password):
    if username == 'admin' and password == '123456':
        return True
    else:
        QtWidgets.QMessageBox.information(None, '登录失败', '用户名或密码错误')
        return False


# 如果天线尺寸设置错误，则弹出信息窗口
def check_size(size):
    _size = [('8', '8'), ('8', '16'), ('8', '32'), ('16', '16'), ('16', '32'), ('16', '64'), ('32', '32'), ('32', '64'),
             ('64', '64')]
    if size not in _size:
        QtWidgets.QMessageBox.information(None, '天线尺寸错误',
                                          '天线尺寸大小应该在以下范围：8x8, 8x16, 8x32, 16x16, 16x32, 16x64, 32x32, 32x64, 64x64')
