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
        # title出力
        # for article in response.css('article.article'):
        #     blog_title = article.css('header.article-header h1 a::text').extract_first()
        #     yield {"title": blog_title}

        # next_url = 'https://lineblog.me/mimori_suzuko/?p=2'
        # yield scrapy.Request(next_url, callback=self.parse)
