#!/usr/bin/python
# -* - coding: UTF-8 -* -
import scrapy
from items import ExamplesItem


class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['twistedmatrix.com']
    start_urls = ['https://twistedmatrix.com/documents/current/core/examples/']

    def parse(self, response):
        urls  = response.css('a.reference.download.internal::attr(href)').extract()
        for url in urls:
            yield ExamplesItem(file_urls = [response.urljoin(url)])


