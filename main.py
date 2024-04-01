from PyQt5.QtWidgets import QApplication, QWidget, QStyle
from bh_window import BHWindow
from bh_utils import *



if __name__ == "__main__":
    app = QApplication([])
    style_sheet = styleS_sheet_loder("bh_style.qss")
    app.setStyleSheet(style_sheet)
    bhw = BHWindow()
    bhw.show()
    app.exec_()