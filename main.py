from PyQt5.QtWidgets import QApplication, QWidget, QStyle
from bh_window import BHWindow
from bh_utils import *
# from qt_material import apply_stylesheet
# from qt_material import list_themes



if __name__ == "__main__":
    app = QApplication([])
    # apply_stylesheet(app, theme='bh_style.xml', invert_secondary=True, css_file="bh_style.qss")
    # print(list_themes())
    style_sheet = styleS_sheet_loder("bh_style.qss")
    app.setStyleSheet(style_sheet)
    bhw = BHWindow()
    bhw.show()
    app.exec_()