#!/usr/bin/python
# -* - coding: UTF-8 -* -
#!python
#coding:utf-8
# -*- coding:utf-8 -*-
import sys
import numpy as np
import hashlib
import datetime,time
import struct,socket


def Ip2Int(ip):
    return struct.unpack("!L",socket.inet_aton(ip))[0]

def sha1(value):
    value = '%s-Last-ip' % value
    return hashlib.sha1(value).hexdigest()
def main():
    class A(object):  # Python2.x 记得继承 object
        def __init__(self):
            print("hello, super")
        def add(self, x):
            y = x + 1
            print(y)

    class B(A):
        def add(self, x):
            super(B, self).add(1)

    class Parent(object):
        def __init__(self, value):
            self.some_var = value

    class Child(Parent):
        def __init__(self, value):
            super(Child, self).__init__(value)

        def doSomething(self):
            parent_var = self.some_var

    b = B()
    b.add(2)
    obj = Child(123)
    obj.doSomething()

def ip2long(ip):
    ip_list=ip.split('.')
    result=0
    for i in range(4):  #0,1,2,3
        result=result+int(ip_list[i])*256**(3-i)
    return result


class solution:

    def restoreIpAddresses(self, s):
        self.res = []
        tmpList = []
        self.dfs(s, tmpList)
        return self.res


    # dfs遍历，s为待处理字段，tmp存储所有ip小段
    def dfs(self, s, tmpList):
        if len(tmpList) == 4:  # 递归出口，凑够4段
            if len(s) == 0:  # s没有剩余，说明找到一个合法ip，否则返回
                self.res.append('.'.join(tmpList))
            return
        for i in range(1, 4):  # 遍历取s的头，长度从1到3
            if i <= len(s):  # 防止越界
                if int(s[:i]) > 255:  # 数字超出范围
                    return
                elif i > 1 and s[0] == '0':  # 除去0开头，且长度大于1情况
                    return
                self.dfs(s[i:], tmpList + [s[:i]])

if __name__ == '__main__':
    a = ''
    for i in range(26):

        a += chr(i + ord('a'))
        print a
    a = solution()
    print a.restoreIpAddresses("25525511135")

