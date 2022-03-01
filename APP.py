import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from client.main import Ui_MainWindow
from client.login import Log_MainWindow

# setupUi负责对界面的大小、位置进行控制，retranslateUi负责对界面的翻译内容进行控制
app = QApplication(sys.argv)

logWin = Log_MainWindow()
logExc = QMainWindow()
logWin.setupUi(MainWindow=logExc)
logWin.retranslateUi(logExc)
logExc.show()

exitCode = app.exec()
print("退出码为：", exitCode)
sys.exit(exitCode)
