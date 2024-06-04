

import random


def NewFrame(frame, lst):  # lst存的是n个随机数

    lst_1 = []

    # 把抽到的单词存入列表

    for i in range(len(lst) - 1):

        if lst[i] in frame.index:
            lst_1.append(frame[lst[i]:lst[i] + 1].values[0])

        if lst[i] == frame.index[-1]:
            lst_1.append(frame[lst[i]:].values[0])

    lst_2 = []

    # 在每行数据中选两个单词，一个作为题目，一个作为答案

    for i in lst_1:

        # 实例化option类
        opt = option()

        # 设置中文
        opt.set_translation(i[0] + i[1])

        # count用来对行列表中的字符串类型数据计数
        count = 0

        for j in i:

            if type(j) == str:
                count += 1

        # 设置正确选项，第一个元素是中文，第二个元素是词性，所以从第三个元素[2]开始
        opt.set_true_option(i[random.randint(2, count - 1)])

        # 移除列表中的正确选项，防止正确选项和题目重复
        i.remove(opt.get_true_option())

        count -= 1

        # 设置题目
        opt.set_option(i[random.randint(2, count - 1)])

        # 将实例化的problem类存入lst_2,此时的opt里面已经有了三个属性
        lst_2.append(opt)

        # 删掉已经用过了的行
        for i in lst:
            frame_1 = frame.drop(i, axis=0)

    return (lst_2, frame_1)

if __name__ == '__main__':
    l=[[i for i in range(5)] for i in range(10)]
    print(l)
    for i in l:
        print(i)
        for j in i:
            print(j)
            i.remove(j)
            print(i)
        #for j in i:
         #   print(i)

