#!/usr/bin/python
# -* - coding: UTF-8 -* -
#!python
#coding:utf-8
import sys
import numpy as np
import hashlib
import datetime,time
import struct,socket
import numpy as np

def ip2long(ip):
    ip_list=ip.split('.')
    result=0
    for i in range(4):  #0,1,2,3
        result=result+int(ip_list[i])*256**(3-i)
    return result


if __name__ == '__main__':  # 这里是混淆矩阵的实现方式
    a = [1, 2, 3, 4]
    b = [1, 3, 2, 4]
    min_rating = min(a + b)
    max_rating = max(a + b)
    print "min_ratring:%d" % (min_rating)
    print a + b
    ratings = max_rating - min_rating + 1
    contri = np.zeros((ratings,ratings))
    print contri
    contri1 = [[0 for i in range(ratings)]
                for j in range(ratings)]
    print contri1
    for c, d in zip(a,b):
        contri[c-min_rating][d-min_rating] += 1
    print contri

