from PyQt5.QtWidgets import QApplication, QWidget, QStyle
from PyQt5.QtGui import QKeyEvent, QMouseEvent, QResizeEvent, QPalette, QColor, QIcon
from bh_window import BHWindow
from bh_utils import *



if __name__ == "__main__":
    app = QApplication([])
    icon = QIcon()
    icon.addFile("./image/counter.png")
    style_sheet = styleS_sheet_loder("bh_style.qss")
    app.setStyleSheet(style_sheet)
    bhw = BHWindow()
    bhw.setWindowIcon(icon)
    bhw.setWindowTitle("bit helper")
    bhw.show()
    app.exec_()