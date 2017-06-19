# -*- coding: utf-8 -*-
import scrapy
from douyu.items import DouyuItem
import json


class DouyumeinvSpider(scrapy.Spider):
    name = "douyu"
    allowed_domains = ["www.douyu.com"]

    offset = 0
    url = "https://www.douyu.com/directory/game/yz?page="

    start_urls = [url + str(offset)]

    def __init__(self, name=None, **kwargs):
        super().__init__(name=None, **kwargs)


    def parse(self, response):
        # 把json格式的数据转换为python格式，data段是列表
        Datas = response.xpath('//*[@id="live-list-contentbox"]/li/a')

        print(len(Datas))
        items =[]
        for data in Datas:
            item = DouyuItem()
            img =data.xpath('./span/img/@data-original').extract()[0]
            name = data.xpath('./div/p/span[1]/text()').extract()[0]
            number = data.xpath('./@data-rid').extract()[0]

            item['nickname'] = name
            item['imagelink'] = img
            item['number'] = number
            items.append(item)
            yield item
        self.offset +=1
        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)


