#!/usr/bin/python
# -* - coding: UTF-8 -* -
from math import ceil


def chunk(lst, size):
    return (map(lambda x:lst[x*size:x*size +size],range(0,int(ceil(len(lst)/float(size))))))


if __name__ == '__main__':
    print chunk([1, 2, 3, 4, 5, 6, 7], 2)
    print type(chunk([1,2,3,4,5,6,7],2))



