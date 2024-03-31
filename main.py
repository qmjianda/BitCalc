from PyQt5.QtWidgets import QApplication, QWidget
from bh_window import BHWindow




if __name__ == "__main__":
    app = QApplication([])

    bhw = BHWindow()
    bhw.show()

    app.exec_()