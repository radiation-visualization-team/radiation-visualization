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
                print(matrix)
            matrix = matrix + '\n'
        print(matrix)
        self.text_edit.setText(matrix)
        self.text_edit.setStyleSheet("font-family: Microsoft YaHei UI;\n font-size: 25px;\n")
