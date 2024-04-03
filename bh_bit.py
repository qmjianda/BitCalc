from PyQt5.QtCore import QEvent, Qt, pyqtSignal
from PyQt5.QtGui import QKeyEvent, QMouseEvent, QResizeEvent, QPalette, QColor
from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel,QApplication
from bh_utils import *

class BHBit(QWidget):
    val_updated = pyqtSignal(int)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_val = 0
        self.m_bit_pos = 0
        self.m_btn_width = 20
        self.m_btn_height = 20
        self.m_label_hidden = True

        self.m_layout = QVBoxLayout()
        self.m_layout.setContentsMargins(0,0,0,0)
        self.m_layout.setSpacing(0)
        self.setLayout(self.m_layout)

        self.m_btn = QPushButton()
        self.m_btn.setFixedSize(self.m_btn_width, self.m_btn_height)
        self.m_btn.setCheckable(True)
        self.m_btn.setObjectName("BHBit_btn")
        self.m_btn.clicked.connect(self.__btn_clicked_slot)
        self.m_layout.addWidget(self.m_btn, 0, Qt.AlignmentFlag.AlignCenter)

        self.m_label = QLabel(str(self.m_bit_pos))
        self.m_label.setHidden(self.m_label_hidden)
        self.m_label.setProperty("light_color", "disable")
        self.m_label.setObjectName("BHBit_label")
        self.m_layout.addWidget(self.m_label, 0, Qt.AlignmentFlag.AlignCenter)

        self.m_clicked_updatable = True

        self.setval(0)
        self.setObjectName("BHBit")

    def __btn_clicked_slot(self, val:bool):
        if(self.m_clicked_updatable):
            self.setval(val)
        else:
            self.setval(self.m_val)
        self.val_updated.emit(self.m_bit_pos)

    def set_clicked_updatable(self, enable:bool):
        self.m_clicked_updatable = enable
        
    def set_disabled(self, disable:bool):
        self.setDisabled(disable)

    def set_bit_pos(self, bit_pos:int):
        bit_pos  = bit_pos % 64
        self.m_bit_pos = bit_pos
        self.m_label.setText(str(self.m_bit_pos))

    def label_set_hidden(self, hidden:bool):
        self.m_label_hidden = hidden
        self.m_label.setHidden(self.m_label_hidden)

    def bit_pos(self):
        return self.m_pos

    def setval(self, val:bool):
        self.m_val = int(val)
        self.m_btn.setChecked(val)
        self.m_btn.setText(str(self.m_val))
        
    def val(self):
        return self.m_val
    
    def enterEvent(self, a0: QEvent) -> None:
        self.m_label.setProperty("light_color", "enable")
        self.m_label.setStyle(QApplication.style())
        self.m_label.setHidden(False)
    
    def leaveEvent(self, a0: QEvent) -> None:
        self.m_label.setProperty("light_color", "disable")
        self.m_label.setStyle(QApplication.style())
        self.m_label.setHidden(self.m_label_hidden)
    