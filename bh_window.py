from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QMouseEvent, QPalette, QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout,QGraphicsDropShadowEffect
from bh_disp import BHDisp
from bh_grid import BHGrid
from bh_calc import BHCalc

class BHWindow(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setFixedSize(400, 500)
        self.m_layout = QVBoxLayout()
        self.m_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.m_layout)

        self.m_disp = BHDisp()
        self.m_layout.addWidget(self.m_disp)

        self.m_calc = BHCalc()
        self.m_calc.val_changed.connect(self.calc_upval_slot)
        self.m_layout.addWidget(self.m_calc)

        self.m_grid = BHGrid()
        self.m_grid.val_updated.connect(self.grid_upval_slot)
        self.m_layout.addWidget(self.m_grid)

        palette = self.palette()
        palette.setColor(QPalette.Background, QColor(255,255, 255))
        self.setPalette(palette)
        # self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint
        #                    | Qt.WindowMaximizeButtonHint)

        
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
        
