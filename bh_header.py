from PyQt5.QtCore import QEvent, Qt, pyqtSignal
from PyQt5.QtGui import QKeyEvent, QMouseEvent, QResizeEvent, QPalette, QColor
from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QLabel,QApplication,QSpacerItem,QSizePolicy
from bh_utils import *

class BHHeader(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("BHHeader")
        self.setFixedHeight(40)
        self.m_layout = QHBoxLayout()
        self.m_layout.setContentsMargins(0,0,0,0)
        self.m_layout.setSpacing(2)
        self.setLayout(self.m_layout)
        
        self.m_spacing = QSpacerItem(20,40, hPolicy=QSizePolicy.Expanding)

        self.m_title = QLabel("bit_helper")
        self.m_title.setObjectName("BHHeader_title")
        self.m_close_btn = QPushButton("x")
        self.m_close_btn.setObjectName("BHHeader_close_btn")
        self.m_minimize_btn = QPushButton("|")
        self.m_minimize_btn.setObjectName("BHHeader_minimize_btn")
        self.m_top_btn = QPushButton("T")
        self.m_top_btn.setObjectName("BHHeader_top_btn")

        self.m_layout.addWidget(self.m_title, alignment=Qt.AlignLeft)
        self.m_layout.addSpacerItem(self.m_spacing)
        self.m_layout.addWidget(self.m_close_btn, alignment=Qt.AlignRight)
        self.m_layout.addWidget(self.m_minimize_btn, alignment=Qt.AlignRight)
        self.m_layout.addWidget(self.m_top_btn, alignment=Qt.AlignRight)
        self.setObjectName("BHHeader")
