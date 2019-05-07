# -*- coding: utf-8 -*-
import scrapy


class MimorinSpider(scrapy.Spider):
    name = 'mimorin'
    allowed_domains = ['lineblog.me/mimori_suzuko']
    start_urls = ['http://lineblog.me/mimori_suzuko/']

    def parse(self, response):
        # title出力
        h1_titles = response.xpath('//h1/a/text()').extract()
        for title in h1_titles:
            print(title+'\n')
