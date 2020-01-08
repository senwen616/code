#!/usr/bin/python
# -* - coding: UTF-8 -* -

import scrapy


class ExamplesItem(scrapy.Item):
    file_urls = scrapy.Field()  # 指定文件下载的连接
    files = scrapy.Field()      #文件下载完成后会往里面写相关的信息



