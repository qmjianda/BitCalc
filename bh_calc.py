from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtCore import pyqtSignal
from bh_utils import logger

class BHCalc(QWidget):
    val_changed = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_layout = QHBoxLayout()
        self.setLayout(self.m_layout)
        self.m_val = 0
        self.m_label = QLabel("=")
        self.m_line_edit = QLineEdit()
        self.m_line_edit.setPlaceholderText("Enter the formula and press Enter")
        self.m_layout.addWidget(self.m_label)
        self.m_layout.addWidget(self.m_line_edit)
        self.m_line_edit.editingFinished.connect(self.calc)
        
    def calc(self):
        formula_str = self.m_line_edit.text()
        try:
            self.m_val = eval(formula_str)
            self.val_changed.emit()
        except Exception as e:
            logger.error(str(e))

    def setval(self, val:int):
        self.m_val = val
        self.m_line_edit.setText(str(val))

    def val(self) -> int:
        return self.m_val