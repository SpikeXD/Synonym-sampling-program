# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:13:39 2024

@author: Lenovo

可以参考PyQt官网的所有模块，地址：
https://www.riverbankcomputing.com/static/Docs/PyQt5/module_index.html#ref-module-index
C++具体实现的API文档，地址：
https://doc.qt.io/qt-5/qtwidgets-module.html
"""
import sys


from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import uic

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=None
        self.init_ui()
    def init_ui(self):
        self.ui=uic.loadUi("E:\Program\PythonProgram\近义词抽查项目\近义词抽查界面\近义词抽查界面.ui")
        #print(self.ui.__dict__)
        
if __name__=='__main__':
    
    app=QApplication(sys.argv)
    
    w=MyWindow()
    
    w.setWindowTitle("近义词抽查界面")
    
    w.ui.show()
    
    app.exec()