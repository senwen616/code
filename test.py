#!/usr/bin/python
# -* - coding: UTF-8 -* -
#!python
#coding:utf-8
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

if __name__ == '__main__':
    #main()
    #print(np.asarray([1,2,3,5]).reshape(1, -1))
    #print (int("12",8))
    '''
    s0 = 'abcdefghijklmnopqrstuvwxyz'
    s2 = [chr(i) for i in range(ord('a'), ord('a')+26, 2)]
    s1 = [chr(i + 97) for i in range(26)]
    s3 = [chr(i + 65) for i in range(26)]
    #s0.decode('gbk')
    dic1 = {}
    dic2 = {}
    for i in s1:
        dic1[i] = 0
        dic2[i] = 0
    print (dic1)
    print (s1)
    print(s2)
    print(s3)
    print(ord('A'), ord('a'))
    '''
    l = np.arange(2,26,2).reshape((2,2,3))
    print l
    l_le = l[:,:-1]
    print l_le
    print l_le.shape
    #print (l[:2])
    #print(sha1(""))
    a = '2019-06-11'
    b = str(datetime.datetime.strptime(a, "%Y-%m-%d"))
    c = time.strptime(b, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(c))
    print b
    print c
    print timeStamp
    print Ip2Int('127.0.0.1')
    print ip2long('127.0.0.1')
