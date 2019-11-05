# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fileDownload.items import FiledownloadItem


class PexelsSpider(CrawlSpider):
    name = 'pexels'
    allowed_domains = ['pexels.com']
    start_urls = ['https://www.pexels.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/photo/'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print("crawl page:"+response.url)
        url = response.xpath("//img[contains(@src,'photos')]/@src").extract()
        item = FiledownloadItem()
        try:
            item['file_urls'] = url
            yield item
        except Exception as  e:
            print(str(e))
