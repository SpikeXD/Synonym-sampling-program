# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 07:31:55 2024

@author: Lenovo
"""
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import uic

from generateProblemList import*

class MyWindow(QWidget):
    
    def __init__(self,fp):
    
        super().__init__()
        
        self.file_path=fp
        
        self.ui=None
        
        self.init_ui()
    
    def init_ui(self):
    
        self.ui = uic.loadUi(self.file_path)
        
class MyQuestionWindow(MyWindow):

    __n = 0

    stylesheet = "QPushButton::hover{\n""background-color:rgb(65,200,255)\n""}"

    stylesheet_TrueChoice = "QPushButton{""background-color:rgb(186,109,32);""}"

    stylesheet_FalseChoice = "QPushButton{""background-color:rgb(147,84,139);""}"

    stylesheet_frame_problem = "QPushButton{\n"
    "height:120px;\n"
    "background-color:rgb(160,160,160);\n"
    "border-radius:25px;\n"
    "border:none;\n"
    "color:rgb(255,255,255);\n"
    "font-size:50px;\n"
    "font-style:none;\n"
    "font: 57 35pt \"Adobe Myungjo Std M\";\n"
    "}\n"
    "QPushButton::hover{\n"
    "background-color:rgb(65,200,255);\n"
    "}"

    # print(__n)
    # print(type(__n))
    def __init__(self,fp,number):

        self.set_n(number)
        
        super().__init__(fp)

        print(self.get_n())

        self.init_ui()
        
    def init_ui(self):
        
        super().init_ui()

        # self.set_n(20)
        # print(self.__n)
        # print(self.get_n())
        # print(type(self.__n))

        #题目标签框
        self.problem_text=self.ui.label_problem
        
        #选项按钮1
        self.btn_option_1=self.ui.pushButton_option_1
        
        #选项按钮2
        self.btn_option_2=self.ui.pushButton_option_2
        
        #选项按钮3
        self.btn_option_3=self.ui.pushButton_option_3
        
        #选项按钮4
        self.btn_option_4=self.ui.pushButton_option_4
        
        #中文提示按钮
        self.btn_translation=self.ui.pushButton_translation

        #文本框
        self.textBw_translation=self.ui.textBrowser_translation

        #下一题按钮
        self.btn_next=self.ui.pushButton_next

        #选项按钮所在的父类
        # self.frame_problem = self.ui.frame_11

        self.frame = ReadExcel()

        print('n=', self.get_n())

        self.lst_n = EmergeRandom(self.get_n(), self.frame)

        self.lst_2, self.frame_1 = NewFrame(self.frame, self.lst_n)

        self.problem_list = ProblemList(self.frame_1, self.get_n(), self.lst_2)

        try:
            self.shuffle_problem_list = shuffleProblemList(self.problem_list)
        except Exception as e:
            print(e)

        # for i in range(len(self.problem_list)):
            # print('第{}题：{}'.format(i,self.problem_list[i].get_subject().get_option()))
        # print(self.problem_list[-1].get_subject().get_option())

        self.i = 0

        # 设置各个按钮的文本内容
        self.refresh_problem()

        # 绑定所有按键和槽函数

        self.btn_translation.clicked.connect(self.clicked_btn_translation)

        self.btn_option_1.clicked.connect(self.clicked_btn_option_1)

        self.btn_option_2.clicked.connect(self.clicked_btn_option_2)

        self.btn_option_3.clicked.connect(self.clicked_btn_option_3)

        self.btn_option_4.clicked.connect(self.clicked_btn_option_4)

        self.btn_next.clicked.connect(self.clicked_btn_next)

    def refresh_problem(self):

        # 设置各个按钮的文本内容
        self.problem_text.setText('第{}题：{}'.format(self.i+1,self.shuffle_problem_list[self.i].get_subject().get_option()))

        self.btn_translation.setText('查看中文意思')

        self.btn_option_1.setText(self.shuffle_problem_list[self.i].get_option_1().get_option())

        self.btn_option_1.setStyleSheet(self.stylesheet_frame_problem)

        self.btn_option_2.setText(self.shuffle_problem_list[self.i].get_option_2().get_option())

        self.btn_option_2.setStyleSheet(self.stylesheet_frame_problem)

        self.btn_option_3.setText(self.shuffle_problem_list[self.i].get_option_3().get_option())

        self.btn_option_3.setStyleSheet(self.stylesheet_frame_problem)

        self.btn_option_4.setText(self.shuffle_problem_list[self.i].get_option_4().get_option())

        self.btn_option_4.setStyleSheet(self.stylesheet_frame_problem)

        # 设置题目状态
        self.sate = self.problem_list[self.i].get_sate()

        # 设置题目文本
        self.subject = self.problem_list[self.i].get_subject()

        self.true_option = self.problem_list[self.i].get_true_option()

        # self.frame_problem.setStyleSheet(self.stylesheet_frame_problem)
        # self.frame_problem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_problem.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_problem.setLineWidth(0)

    #定义判断函数
    def jude(self,txt):
        
        if txt == self.true_option.get_option():
        
            return True
        
        else:
        
            return False
    #定义槽函数
    def clicked_btn_option_1(self):
        
        txt = self.btn_option_1.text()

        if txt == self.shuffle_problem_list[self.i].get_option_1().get_option():

            self.btn_option_1.setText(self.shuffle_problem_list[self.i].get_option_1().get_translation())

        else:

            self.btn_option_1.setText(self.shuffle_problem_list[self.i].get_option_1().get_option())

        if self.shuffle_problem_list[self.i].get_option_1().get_true_option() == self.shuffle_problem_list[self.i].get_option_1().get_option():

            self.textBw_translation.setText('选对了')

            self.btn_option_1.setStyleSheet(self.stylesheet_TrueChoice+self.stylesheet)

        else:

            self.textBw_translation.setText('选错了')

            self.btn_option_1.setStyleSheet(self.stylesheet_FalseChoice+self.stylesheet)

        bol = self.jude(txt)
        
        return bol
    def clicked_btn_option_2(self):
         
        txt=self.btn_option_2.text()

        if txt == self.shuffle_problem_list[self.i].get_option_2().get_option():

            self.btn_option_2.setText(self.shuffle_problem_list[self.i].get_option_2().get_translation())

        else:

            self.btn_option_2.setText(self.shuffle_problem_list[self.i].get_option_2().get_option())

        if self.shuffle_problem_list[self.i].get_option_2().get_true_option() == self.shuffle_problem_list[self.i].get_option_2().get_option():

            self.textBw_translation.setText('选对了')

            self.btn_option_2.setStyleSheet(self.stylesheet_TrueChoice+self.stylesheet)

        else:

            self.textBw_translation.setText('选错了')

            self.btn_option_2.setStyleSheet(self.stylesheet_FalseChoice+self.stylesheet)

        bol=self.jude(txt)
        
        return bol
    def clicked_btn_option_3(self):
        
        txt = self.btn_option_3.text()

        if txt == self.shuffle_problem_list[self.i].get_option_3().get_option():

            self.btn_option_3.setText(self.shuffle_problem_list[self.i].get_option_3().get_translation())

        else:

            self.btn_option_3.setText(self.shuffle_problem_list[self.i].get_option_3().get_option())

        if self.shuffle_problem_list[self.i].get_option_3().get_true_option() == self.shuffle_problem_list[self.i].get_option_3().get_option():

            self.textBw_translation.setText('选对了')

            self.btn_option_3.setStyleSheet(self.stylesheet_TrueChoice+self.stylesheet)

        else:

            self.textBw_translation.setText('选错了')

            self.btn_option_3.setStyleSheet(self.stylesheet_FalseChoice+self.stylesheet)

        bol = self.jude(txt)
        
        return bol
    def clicked_btn_option_4(self):
         
        txt = self.btn_option_4.text()

        if txt == self.shuffle_problem_list[self.i].get_option_4().get_option():

            self.btn_option_4.setText(self.shuffle_problem_list[self.i].get_option_4().get_translation())

        else:

            self.btn_option_4.setText(self.shuffle_problem_list[self.i].get_option_4().get_option())

        bol = self.jude(txt)
        
        if self.shuffle_problem_list[self.i].get_option_4().get_true_option() == self.problem_list[self.i].get_option_4().get_option():

            self.textBw_translation.setText('选对了')

            self.btn_option_4.setStyleSheet(self.stylesheet_TrueChoice+self.stylesheet)

        else:

            self.textBw_translation.setText('选错了')

            self.btn_option_4.setStyleSheet(self.stylesheet_FalseChoice+self.stylesheet)

        # print(self.shuffle_problem_list[self.i].get_option_4().get_true_option())
        # print(self.shuffle_problem_list[self.i].get_option_4().get_option())
        # print(self.shuffle_problem_list[self.i].get_option_4().get_translation())
        # self.textBw_translation.repaint()

        return bol
    def clicked_btn_translation(self):
         
        # txt = self.btn_translation.text()

        # self.btn_translation.setText(self.true_option.get_translation())

        self.textBw_translation.setText(self.true_option.get_translation())
         
        # print(txt)
    def clicked_btn_next(self):

        self.i += 1
        try:
            # print(type(self.get_n()))
            print('n=',self.get_n())
            if self.i < self.get_n():

                # print(self.i)
                # print('self.temp_problem.get_true_option().get_option()=',self.temp_problem.get_true_option().get_option())

                print('第{}题：{}'.format(self.i, self.shuffle_problem_list[self.i].get_true_option().get_option()))

                # 设置各个按钮的文本内容
                self.refresh_problem()

                self.textBw_translation.setText('')

            else:
                print(self.i)

                self.i = self.get_n()-1

                self.textBw_translation.setText('已经是最后一题了')

                w2.ui.show()

                self.ui.close()

        except Exception as e:

            print(e)
    def set_n(self,number):
        self.__n = number
    def get_n(self):
        return self.__n

class ChoiceNumberWindow(MyWindow):
    def __init__(self, fp):
        super().__init__(fp)
        self.init_ui()

    def init_ui(self):
        super().init_ui()

        self.btn_1 = self.ui.pushButton
        self.btn_2 = self.ui.pushButton_2
        self.btn_3 = self.ui.pushButton_3
        self.btn_4 = self.ui.pushButton_4
        self.linedit = self.ui.lineEdit
        self.btn_start = self.ui.pushButton_start
        self.btn_1.clicked.connect(self.clicked_btn_1)
        self.btn_2.clicked.connect(self.clicked_btn_2)
        self.btn_3.clicked.connect(self.clicked_btn_3)
        self.btn_4.clicked.connect(self.clicked_btn_4)
        self.linedit.returnPressed.connect(self.linedit_return_pressed)
        self.btn_start.clicked.connect(self.clicked_btn_start)
    def clicked_btn_1(self):

        self.linedit.setText(self.btn_1.text())

        self.n = int(self.linedit.text())

        print(self.n)
    def clicked_btn_2(self):

        self.linedit.setText(self.btn_2.text())

        self.n = int(self.linedit.text())

        print(self.n)
    def clicked_btn_3(self):

        self.linedit.setText(self.btn_3.text())

        self.n = int(self.linedit.text())

        print(self.n)
    def clicked_btn_4(self):

        self.linedit.setText(self.btn_4.text())

        self.n = int(self.linedit.text())

        print(self.n)
    def linedit_return_pressed(self):

        self.n = int(self.linedit.text())

        print(self.n)

    def clicked_btn_start(self):

        try:
            self.n = int(self.linedit.text())
        except Exception as e:
            print(e)
        else:
            print(self.n)

        global w3

        global w2

        w3 = MyQuestionWindow(fp_3, self.n)

        # print('w3.n={}'.format(w3.get_n()))

        w3.ui.show()

        w2.ui.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    fp_1 = "E:\Program\PythonProgram\近义词抽查项目\近义词抽查界面\开始界面.ui"

    fp_2 = "E:\Program\PythonProgram\近义词抽查项目\近义词抽查界面\近义词单词抽查选择单词数界面.ui"

    fp_3 = "E:\Program\PythonProgram\近义词抽查项目\近义词抽查界面\近义词抽查界面.ui"

    fp_4 = "E:\Program\PythonProgram\近义词抽查项目\近义词抽查界面\近义词抽查结束界面.ui"

    w2 = ChoiceNumberWindow(fp_2)

    w2.ui.show()

    app.exec()
















