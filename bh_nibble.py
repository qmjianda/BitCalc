from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from bh_bit import BHBit

class BHNibble(QWidget):
    val_updated = pyqtSignal(int)
    def __init__(self, base, parent=None):
        super().__init__(parent)
        self.m_base = base
        self.m_layout = QHBoxLayout()
        self.m_layout.setContentsMargins(0,0,0,0)
        self.m_layout.setSpacing(0)
        self.setLayout(self.m_layout)

        self.m_width = 80
        self.m_height = 60
        self.setFixedSize(self.m_width, self.m_height)

        self.m_bits = []
        
        for i in range(4):
            bit = BHBit()
            bit.set_bit_pos(self.m_base + i)
            bit.val_updated.connect(self.__val_updated_slot)
            if(i == 0):
                bit.label_set_hidden(False)
            self.m_bits.append(bit)
        
        for i in range(3, -1, -1):
            self.m_layout.addWidget(self.m_bits[i], 0, Qt.AlignmentFlag.AlignTop)
    
    def __val_updated_slot(self, pos):
        self.val_updated.emit(pos)

    def base(self):
        return self.m_base

