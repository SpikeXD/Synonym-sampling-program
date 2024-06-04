"""
该.py文件封装了近义词抽查程序的方法
"""

import pandas as pd
import random

from problem import problem,option

#读取.xlsx文件
def ReadExcel(path=r"C:\Users\Lenovo\Desktop\近义词.xlsx"):

    frame = pd.read_excel(path)

    return frame
#获取抽查单词个数的随机数个数
def EmergeRandom(n, frame):

    lst = []

    while len(lst) < n:

        ran = random.randint(0, frame.index[-1]-1)

        if ran not in lst and ran in frame.index:

            lst.append(ran)

    return lst

def NewFrame(frame, lst):  # lst存的是n个随机数

    lst_1 = []

    # 把抽到的单词存入列表

    for i in range(len(lst)):

        lst_1.append(frame.values[lst[i]])

    lst_2 = []

    # 在每行数据中选两个单词，一个作为题目，一个作为答案
    for i in range(len(lst_1)):

        # 实例化option类
        opt = option()

        # 设置中文
        opt.set_translation(lst_1[i][1] + lst_1[i][0])

        # count用来对行列表中的字符串类型数据计数
        count = 0

        for j in lst_1[i]:

            if type(j) == str:
                count += 1

        # 设置正确选项，第一个元素是中文，第二个元素是词性，所以从第三个元素[2]开始
        opt.set_true_option(lst_1[i][random.randint(2, count - 1)])

        # 移除列表中的正确选项，防止正确选项和题目重复
        lst_1[i] = (list(lst_1[i]))
        lst_1[i].remove(opt.get_true_option())

        count -= 1

        # 设置题目
        opt.set_option(lst_1[i][random.randint(2, count - 1)])

        # 将实例化的problem类存入lst_2,此时的opt里面已经有了三个属性
        lst_2.append(opt)

        # 删掉已经用过了的行
        for i in lst:
            frame_1 = frame.drop(i, axis=0)

    return (lst_2, frame_1)

    #获取本次要抽查的单词个数

def ChooseNumber():

    number=int(input("请选择本次考察的单词数:"))

    return number

    #将抽到的单词行数据集合到一个列表中
# 加入错误答案
def ProblemList(frame,n,option_list):

    lst = EmergeRandom(n*3,frame)

    # print(len(lst))
    # frame 一次处理后的数据
    # lst储存3xn的随机数
    # option_list储存题目

    # 把抽到的单词行存入列表
    lst_1 = []

    FalseOption=[]

    Problem_list=[]

    # 将frame转化为lst_1
    for i in range(len(lst)):

        lst_1.append(frame.values[lst[i]])

    #print('len(lst_1)=',len(lst_1))
    #print('len(option_list)=',len(option_list))

    # print('len(lst_1)=',len(lst_1))

    for i in range(len(lst_1)):
        #print(i)
        # 实例化option类
        false_option = option()

        # 设置选项的真确选项
        false_option.set_true_option(option_list[i//3].get_true_option())

        #设置选项的中文
        #print(lst_1[0],'\n',lst_1[1],end='')
        false_option.set_translation(lst_1[i][1]+lst_1[i][0])

        # count用来对行列表中的字符串类型数据计数
        count = 0

        for j in lst_1[i]:

            if type(j) == str:

                count += 1

        # 设置选项的英文
        false_option.set_option(lst_1[i][random.randint(2,count-1)])

        # 将错误选项添加到列表中
        FalseOption.append(false_option)

        #print(false_option.get_option())

    for i in range(len(option_list)):

        # 将设置题目和正确选项
        problem1 = problem()

        problem1.set_subject(option_list[i])

        problem1.set_true_option(option_list[i])

        # problem1.set_option_4(option_list[i])

        problem1.get_option_4().set_option(option_list[i].get_true_option())

        problem1.get_option_4().set_true_option(option_list[i].get_true_option())

        problem1.get_option_4().set_translation(option_list[i].get_translation())

        # 设置错误选项
        for j in range(len(FalseOption)):

            if FalseOption[j].get_true_option() == option_list[i].get_true_option() and j // 3 == i and problem1.get_option_1().get_option() == '':

                problem1.set_option_1(FalseOption[j])

            elif FalseOption[j].get_true_option() == option_list[i].get_true_option() and j // 3 == i and problem1.get_option_2().get_option() == '':

                problem1.set_option_2(FalseOption[j])

            elif FalseOption[j].get_true_option() == option_list[i].get_true_option() and j // 3 == i and problem1.get_option_3().get_option() == '':

                problem1.set_option_3(FalseOption[j])

            else:

                pass

        Problem_list.append(problem1)

    return Problem_list

def shuffleProblemList(problem_list):

    for i in range(len(problem_list)):
        l = [problem_list[i].get_option_1(),problem_list[i].get_option_2(),problem_list[i].get_option_3(),problem_list[i].get_option_4()]
        random.shuffle(l)
        problem_list[i].set_option_1(l[0])
        problem_list[i].set_option_2(l[1])
        problem_list[i].set_option_3(l[2])
        problem_list[i].set_option_4(l[3])

    return problem_list