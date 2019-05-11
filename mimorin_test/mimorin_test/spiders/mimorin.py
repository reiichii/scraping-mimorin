# -*- coding: utf-8 -*-
import scrapy
import sys
from mimorin_test.items import MimorinItem

class MimorinSpider(scrapy.Spider):
    name = 'mimorin'
    allowed_domains = ['lineblog.me']
    start_urls = ['https://lineblog.me/mimori_suzuko/']
    current_page = 1


    def parse(self, response):
        # そのページの画像を取得
        item = MimorinItem()
        item['image_urls'] = []
        for image_url in response.css('img.pict::attr(src)').extract():
            item['image_urls'].append(image_url)
        print(item)

        #総ページ数を取得
        total_page = response.css('li.paging-last a::text').extract_first()
        if total_page is None:
            sys.exit()

        # 総ページ分回してurlを生成
        if self.current_page <= 5:
            self.current_page += 1
            next_url = 'https://lineblog.me/mimori_suzuko/?p=' + str(self.current_page)
            yield scrapy.Request(next_url, callback=self.parse)
