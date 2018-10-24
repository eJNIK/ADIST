from PyQt5.QtWidgets import QApplication
from Tools import argv, exit
from MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(argv)
    w = MainWindow()
    exit(app.exec_())
