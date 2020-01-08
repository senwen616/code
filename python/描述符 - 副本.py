#!/usr/bin/python
# -* - coding: UTF-8 -* -

"""
class Score:
    def __init__(self, default=0):
        self._score = default

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Score must be integer')
        if not 0 <= value <= 100:
            raise ValueError('Valid value must be in [0, 100]')

        self._score = value

    def __get__(self, instance, owner):
        print 'get'
        return self._score

    def __del__(self):
        del self._score


class Student:
    math = Score(0)
    chinese = Score(0)
    english = Score(0)

    def __init__(self, name, math, chinese, english):
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english

    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {}, english:{}>".format(
            self.name, self.math, self.chinese, self.english
        )

"""

class revealAccess:
    def __init__(self, initval = None, name = 'var'):
        self.val = initval
        self.name = name
    def __get__(self, obj, objtype):
        print("Retrieving",self.name)
        return self.val
    def __set__(self, obj, val):
        print("updating",self.name)
        self.val = val
class myClass:
    x = revealAccess(10,'var "x"')
    y = 5

if __name__ == '__main__':

    # std1 = Student('小红', 89, '-20', 60)
    # print std1.chinese
    m = myClass()
    print(m.x)
    m.x = 20
    print(m.x)
    print(m.y)


