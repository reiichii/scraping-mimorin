# -*- coding: utf-8 -*-
import scrapy
from mimorin_test.items import MimorinItem

class MimorinSpider(scrapy.Spider):
    name = 'mimorin'
    allowed_domains = ['lineblog.me']
    start_urls = ['https://lineblog.me/mimori_suzuko/']


    def parse(self, response):
        # そのページの画像を取得
        item = MimorinItem()
        item['image_urls'] = []
        for image_url in response.css('img.pict::attr(src)').extract():
            item['image_urls'].append(image_url)

        return item

        # next_url = 'https://lineblog.me/mimori_suzuko/?p=2'
        # yield scrapy.Request(next_url, callback=self.parse)
