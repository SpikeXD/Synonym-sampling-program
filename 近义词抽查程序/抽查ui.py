# -*- coding: utf-8 -*-
"""
Created on Sat May 25 15:14:25 2024

@author: Lenovo
"""

import sys


from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

if __name__=='__main__':
    app=QApplication(sys.argv)
    
    ui=uic.loadUi("E:\近义词抽查项目\近义词抽查界面\开始界面.ui")
    
    ui.show()
    
    app.exec()