# coding:utf8

import scrapy


class ItemSpider(scrapy.Spider):
    name = 'itemSpider'

    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):
        mingyan = response.css('div.quote')

        for v in mingyan:
            text = v.css('.text::text').extract_first()

            author = v.css('.author::text').extract_first()
            tags = v.css('.tags .tag::text').extract()
            tags = ','.join(tags)

            filename = '%s - 语录.txt' % author

            # f = open(filename, 'a+')
            with open(filename, 'a+') as f:
                f.write(text)
                f.write('\n')
                f.write('标签：' + tags)
                f.close()

        next_page = response.css('li.next a::attr(href)').extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
