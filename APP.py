import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from client.main import Ui_MainWindow


# setupUi负责对界面的大小、位置进行控制，retranslateUi负责对界面的翻译内容进行控制
app = QApplication(sys.argv)
# 创建并运行主界面
mnWin = Ui_MainWindow()
mnExc = QMainWindow()
mnWin.setupUi(MainWindow=mnExc)
mnWin.retranslateUi(mnExc)
mnExc.show()

exitCode = app.exec()
print("退出码为：", exitCode)
sys.exit(exitCode)
