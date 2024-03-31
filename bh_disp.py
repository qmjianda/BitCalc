from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from bh_utils import *

class Displabel(QWidget):
    def __init__(self, name:str, parent=None) -> None:
        super().__init__(parent)
        self.m_name = name
        self.m_layout = QHBoxLayout()
        self.m_layout.setContentsMargins(0,0,0,0)
        self.m_layout.setSpacing(0)
        self.setLayout(self.m_layout)
        self.m_head = QLabel(self.m_name)
        self.m_layout.addWidget(self.m_head, stretch=0)
        self.m_disp = QLabel()
        self.m_layout.addWidget(self.m_disp, stretch=1)
        self.m_disp.setWordWrap(True)

    
    def settext(self, text:str):
        self.m_disp.setText(text)


class BHDisp(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.m_layout = QVBoxLayout()
        self.m_layout.setContentsMargins(0,0,0,0)
        # self.m_layout.setSpacing(20)
        self.setLayout(self.m_layout)
        
        self.m_hex_label = Displabel("HEX\t")
        self.m_dec_label = Displabel("DEC\t")
        self.m_oct_label = Displabel("OCT\t")
        self.m_bin_label = Displabel("BIN\t")

        self.m_layout.addWidget(self.m_hex_label)
        self.m_layout.addWidget(self.m_dec_label)
        self.m_layout.addWidget(self.m_oct_label)
        self.m_layout.addWidget(self.m_bin_label)

    def setval(self, val:int):
        self.m_hex_label.settext(repeat_insert_str(hex(val)[2:].upper(), " ", 4))
        self.m_dec_label.settext(repeat_insert_str(str(val), ",", 3))
        self.m_oct_label.settext(repeat_insert_str(oct(val)[2:], ",", 3))
        self.m_bin_label.settext(repeat_insert_str(bin(val)[2:], " ", 4, "0"))