from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QPixmap
from bh_window import BHWindow
from bh_utils import *



if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication([])
    map = QPixmap()
    map.load('image/icon.png')
    style_sheet = style_sheet_loder("qss/default_style.qss")
    app.setStyleSheet(style_sheet)
    bhw = BHWindow()
    bhw.setWindowIcon(QIcon(map))
    bhw.setWindowTitle("bit helper")
    bhw.show()
    app.exec_()