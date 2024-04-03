from PyQt5.QtCore import Qt,QRectF
from PyQt5.QtGui import QKeyEvent, QMouseEvent, QPaintEvent, QPalette, QColor,QPainter,QPainterPath,QRegion,QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout,QGraphicsDropShadowEffect,QStyleOption
from bh_disp import BHDisp
from bh_grid import BHGrid
from bh_calc import BHCalc
from bh_header import BHHeader

class BHWindow(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setFixedSize(400, 500)
        self.m_layout = QVBoxLayout()
        self.m_layout.setContentsMargins(10,10,10,10)
        self.setLayout(self.m_layout)

        # self.m_header = BHHeader(self)
        # self.m_layout.addWidget(self.m_header, alignment=Qt.AlignTop)

        self.m_disp = BHDisp()
        self.m_layout.addWidget(self.m_disp)

        self.m_calc = BHCalc()
        self.m_calc.val_changed.connect(self.calc_upval_slot)
        self.m_layout.addWidget(self.m_calc)

        self.m_grid = BHGrid()
        self.m_grid.val_updated.connect(self.grid_upval_slot)
        self.m_layout.addWidget(self.m_grid)

        # self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint
        #                    | Qt.WindowMaximizeButtonHint)
        
        self.setObjectName("BHWindow")

        
    def calc_upval_slot(self):
        val = self.m_calc.val()
        self.m_disp.setval(val)
        self.m_grid.setval(val)

    def grid_upval_slot(self):
        val = self.m_grid.val()
        self.m_disp.setval(val)
        self.m_calc.setval(val)

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if(a0.key() == Qt.Key.Key_Shift):
            self.m_grid.set_clicked_updatable(False)
        elif(a0.key() == Qt.Key.Key_Escape):
            self.m_grid.clr_enabled_range()

    
    def keyReleaseEvent(self, a0: QKeyEvent) -> None:
        if(a0.key() == Qt.Key.Key_Shift):
            self.m_grid.set_clicked_updatable(True)
        


