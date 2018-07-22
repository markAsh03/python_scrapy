# coding:utf8

import scrapy


class mingyan(scrapy.Spider):
    name = "mingyan"  # 定义蜘蛛名称  # 入口方法


    def start_requests(self):
        # 定义爬虫链接
        urls = ['http://lab.scrapyd.cn/page/1/',
                'http://lab.scrapyd.cn/page/2/', ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'mingyan-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('保存文件：%s' % filename)
