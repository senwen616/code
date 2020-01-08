#!/usr/bin/python
# -* - coding: UTF-8 -* -

import urllib

import sys
from bs4 import BeautifulSoup
import re
import os

path = []


def extract(url):
    content = urllib.urlopen(url).read()
    # reg = r'(?:href|HREF)="?((?:http://)?.+?\.txt)'
    reg = r'<a href="(.*)">.*'
    url_re = re.compile(reg)
    url_lst = re.findall(url_re, content)

    for lst in url_lst:
        ext = lst.split('.')[-1]

        if ext[-1] == '/':
            newUrl = url + lst
            extract(newUrl)
        else:
            path.append(url + lst)


print "downloading with urllib"
url = 'https://www.daokers.com/down/'
extract(url)

filePath = 'E:/work/webshell_detection_new/Samples/20191127/new'
filePath = unicode(filePath, 'utf8')

for p in path:
    fileTitle = p.split('/new')[-1]
    file = filePath + fileTitle
    dir = os.path.dirname(file)
    isExists = os.path.exists(dir)

    if isExists == False:
        os.makedirs(dir)
    urllib.urlretrieve(p, file)



