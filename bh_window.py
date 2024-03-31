from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QMouseEvent
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from bh_disp import BHDisp
from bh_grid import BHGrid
from bh_calc import BHCalc

class BHWindow(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setGeometry(200, 300, 500, 500)
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

        self.m_select_mode = False
        self.m_select_cnt = 0
        
    def calc_upval_slot(self, val):
        self.m_disp.setval(val)
        self.m_grid.setval(val)

    def grid_upval_slot(self, pos):
        if(self.m_select_mode):
            if(self.m_select_cnt == 0):
                self.m_select_cnt = 1
                self.m_grid.set_enabled(pos, 63)
            else:
                start_pos = self.m_grid.enabled_start_pos()
                self.m_grid.set_enabled(start_pos, pos)
                self.m_select_cnt = 0
        self.update_val()


    def update_val(self):
        val = self.m_grid.val()
        self.m_disp.setval(val)
        self.m_calc.setval(val)

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if(a0.key() == Qt.Key.Key_Shift):
            self.m_grid.set_clicked_updatable(False)
            self.m_select_mode = True
    
    def keyReleaseEvent(self, a0: QKeyEvent) -> None:
        if(a0.key() == Qt.Key.Key_Shift):
            self.m_grid.set_clicked_updatable(True)
            self.m_select_mode = False
            self.m_select_cnt = 0

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if(a0.button() == Qt.MouseButton.RightButton):
            self.m_select_cnt = 0
            self.m_grid.set_enabled()
            self.update_val()
        return super().mousePressEvent(a0)