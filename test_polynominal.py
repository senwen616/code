#!/usr/bin/python
# -* - coding: UTF-8 -* -
#!python
#coding:utf-8
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

X = np.arange(20).reshape(2, 10)
poly = PolynomialFeatures(degree=2)
res = poly.fit_transform(X)
print res

