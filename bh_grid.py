from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from bh_utils import *
from bh_nibble import BHNibble

class BHGrid(QWidget):
    val_updated = pyqtSignal(int)
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.m_layout = QGridLayout()
        self.m_layout.setContentsMargins(0,0,0,0)
        self.m_layout.setSpacing(10)
        self.setLayout(self.m_layout)

        self.m_bits = []
        self.m_nibbles = []
        for i in range(4):
            for j in range(4):
                nibble = BHNibble((i*4+j)*4)
                self.m_bits += nibble.m_bits
                nibble.val_updated.connect(self.__val_update_slot)
                self.m_nibbles.append(nibble)
                self.m_layout.addWidget(nibble, 3-i, 3-j)

        self.m_enabled_start_pos = 0
        self.m_enabled_end_pos = 64
        self.set_enabled()

    def val(self)->int:
        v = 0
        for index, bit in enumerate(self.m_bits):
            v |= bit.val() << index
        
        v &= self.m_enable_mask
        v >>= self.m_enabled_start_pos
        return v
    
    def setval(self, val:int):
        val <<= self.m_enabled_start_pos
        val &= self.m_enable_mask
        for index, bit in enumerate(self.m_bits):
            bit.setval((val & (1<<index)) != 0)

    def bitval(self, pos):
        pos = min(pos, 63)
        return self.m_bits[pos].val()
    
    def set_bitval(self, pos, val):
        pos = min(pos, 63)
        self.m_bits[pos].setval(val)

    def __enable_by_mask(self, mask:int):
        self.m_enable_mask = mask
        for index, bit in enumerate(self.m_bits):
            if((mask & (1<<index)) != 0):
                bit.set_disabled(False)
            else:
                bit.set_disabled(True)
    
    def set_enabled(self, start=0, end=63):
         self.m_enabled_start_pos = min(max(start, 0), 63)
         self.m_enabled_end_pos = min(max(end, 0), 63)
         mask = 0xFFFF_FFFF_FFFF_FFFF
         mask &= ~((1<<start)-1)
         mask &= (1<<end+1)-1
         self.__enable_by_mask(mask)

    def enabled_mask(self):
        return self.m_enable_mask
    
    def enabled_start_pos(self):
        return self.m_enabled_start_pos
    
    def enabled_end_pos(self):
        return self.m_enabled_end_pos

    def set_clicked_updatable(self, updatable: bool):
        for bit in self.m_bits:
            bit.set_clicked_updatable(updatable)

    def __val_update_slot(self, pos):
        print(pos, self.bitval(pos))
        self.val_updated.emit(pos)