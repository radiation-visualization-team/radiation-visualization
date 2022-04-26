from PyQt5 import QtCore, QtGui, QtWidgets


class Matrix_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet("background-color:white")
        Form.resize(591, 361)
        self.text_edit = QtWidgets.QTextEdit(Form)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.text_edit.setObjectName("text_edit")
        self.horizontalLayout.addWidget(self.text_edit)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.text_edit.setText(_translate("Form", "生成全部矩阵"))

    def matrix_process(self, raw_matrix):
        matrix = ""
        for row in raw_matrix:
            for c in row:
                matrix = matrix + '{} '.format(c)
            matrix = matrix + '\n'
        self.text_edit.setText(matrix)
        self.text_edit.setStyleSheet("font-family: Microsoft YaHei UI;\n font-size: 25px;\n")


class Sub_MatrixForm(object):
    def setupUi(self, Form, xy):
        Form.setObjectName("Form")
        Form.setStyleSheet("background-color:white")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.editList = []
        for _, size in enumerate(
                [('8', '8'), ('8', '16'), ('8', '32'), ('16', '16'), ('16', '32'), ('16', '64'), ('32', '32'),
                 ('32', '64'), ('64', '64')]):
            if size == xy:
                Form.resize(500, 500)
                break
        x, y = int(int(xy[0])/8), int(int(xy[1])/8)
        positions = [(i, j) for i in range(x) for j in range(y)]
        for position in positions:
            temp = QtWidgets.QTextEdit(Form)
            temp.setObjectName("textEdit_{}_{}".format(position[0], position[1]))
            self.editList.append(temp)
            self.gridLayout.addWidget(temp, *position)

        self.horizontalLayout.addLayout(self.gridLayout)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
