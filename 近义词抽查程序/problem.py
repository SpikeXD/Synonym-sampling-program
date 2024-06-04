"""
该.py封装了 option类和 problem类
"""

class option():
    def __init__(self):
        self.translation = ''
        self.true_option = ''
        self.option = ''
        self.sate = 0

    def set_translation(self, translation):
        self.translation = translation

    def get_translation(self):
        return self.translation

    def set_true_option(self, true_option):
        self.true_option = true_option

    def get_true_option(self):
        return self.true_option

    def set_option(self, option):
        self.option = option

    def get_option(self):
        return self.option

    def set_sate(self, sate):
        self.sate = sate

    def get_sate(self):
        return self.sate
class problem():

    def __init__(self):
        self.option_1 = option()

        self.option_2 = option()

        self.option_3 = option()

        self.option_4 = option()

        # 正确选项
        self.true_option = option()

        # 抽查的单词
        self.subject = option()

        # 抽查单词的中文
        self.translation = self.subject.get_translation()

        # 题目的状态（答对/没答/答错）
        self.sate = 0

    def set_translation(self, trans):
        self.translation = trans

    def get_translation(self):
        return self.translation

    def set_subject(self, sub):
        self.subject = sub

    def get_subject(self):
        return self.subject

    def set_sate(self, sa):
        self.sate = sa

    def get_sate(self):
        return self.sate

    def set_true_option(self, t_op):
        self.true_option = t_op

    def get_true_option(self):
        return self.true_option

    def set_option_1(self, op1):
        self.option_1 = op1

    def get_option_1(self):
        return self.option_1

    def set_option_2(self, op2):
        self.option_2 = op2

    def get_option_2(self):
        return self.option_2

    def set_option_3(self, op3):
        self.option_3 = op3

    def get_option_3(self):
        return self.option_3

    def set_option_4(self, op4):
        self.option_4 = op4

    def get_option_4(self):
        return self.option_4

