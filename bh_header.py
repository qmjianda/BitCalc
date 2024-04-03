from PyQt5.QtCore import QEvent, Qt, pyqtSignal, QPoint
from PyQt5.QtGui import QKeyEvent, QMouseEvent, QResizeEvent, QPalette, QColor
from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QLabel,QApplication,QSpacerItem,QSizePolicy
from bh_utils import *

class BHHeader(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_parent = parent
        self.setObjectName("BHHeader")
        self.m_layout = QHBoxLayout()
        self.m_layout.setContentsMargins(0,0,0,0)
        self.m_layout.setSpacing(2)
        self.setLayout(self.m_layout)
        
        self.m_spacing = QSpacerItem(20,40, hPolicy=QSizePolicy.Expanding)

        self.m_title = QLabel()
        self.m_title.setObjectName("BHHeader_title")

        self.m_top_btn = QPushButton()
        self.m_top_btn.setObjectName("BHHeader_top_btn")
        self.m_top_btn.setCheckable(True)
        self.m_top_btn.clicked.connect(self.__top_btn_slot)

        self.m_minimize_btn = QPushButton()
        self.m_minimize_btn.setObjectName("BHHeader_minimize_btn")
        self.m_minimize_btn.clicked.connect(self.__minimize_btn_slot)

        self.m_close_btn = QPushButton()
        self.m_close_btn.setObjectName("BHHeader_close_btn")
        self.m_close_btn.clicked.connect(QApplication.exit)
        
        self.m_layout.addWidget(self.m_title, alignment=Qt.AlignLeft)
        self.m_layout.addSpacerItem(self.m_spacing)
        self.m_layout.addWidget(self.m_top_btn, alignment=Qt.AlignRight)
        self.m_layout.addWidget(self.m_minimize_btn, alignment=Qt.AlignRight)
        self.m_layout.addWidget(self.m_close_btn, alignment=Qt.AlignRight)
        self.setObjectName("BHHeader")
        self.m_drag_enable = False
        self.m_drag_start_point = QPoint()

    def __minimize_btn_slot(self):
        self.m_parent.showMinimized()
        self.m_parent.showNormal()

    def __top_btn_slot(self, checked):
        if not checked:
            self.m_parent.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint
                           | Qt.WindowMaximizeButtonHint)
        else:
            self.m_parent.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint
                           | Qt.WindowMaximizeButtonHint|Qt.WindowStaysOnTopHint)
        self.m_parent.show()

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if(a0.button() == Qt.MouseButton.LeftButton):
            logger.info(f"LeftButton Pressed")
            self.m_drag_start_point = a0.globalPos() - self.m_parent.pos()
            self.m_drag_enable = True
    
    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        if(a0.button() == Qt.MouseButton.LeftButton):
            logger.info(f"LeftButton Released")
            self.m_drag_enable = False
    
    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        if(self.m_drag_enable):
            logger.info(a0.globalPos())
            self.m_parent.move(a0.globalPos() - self.m_drag_start_point)
            