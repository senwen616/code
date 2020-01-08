#!/usr/bin/python
# -* - coding: UTF-8 -* -


class Score:

    def __init__(self,default=0):
        self._score = default

    def __set__(self, instance, value):
        if not isinstance(int, value):
            raise TypeError('value must be integer')
        if not 0 <= value <= 100:
            raise ValueError('value must between 0 and 100')
        self._score = value

    def __get__(self, instance, owner):
        return self.score

    def __del__(self):
        del self._score


class Student:
    math = Score(0)
    chinese = Score(0)

    def __init__(self, name, math, chinese):
        self.name = name
        self.chinese = chinese
        self.math = math

    def __repr__(self):
        return '<student:{},math:{},chinese:{}'.format(self.name, self.math, self.chinese)


if __name__ == '__main__':

    std1 = Student('小红', 89, -20)
    print std1


