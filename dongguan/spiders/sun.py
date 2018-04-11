# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem
"""
爬取东莞阳光网投诉帖子内容
"""
#有点不喜欢使用这个CrawlSpider类写爬虫，不按顺序爬，难以掌控过程，应该是学的太浅了吧。。。
class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'question/\d+/\d+.shtml'), callback= 'parse_item', follow='False')
    )
    def parse_item(self, response):
        item = DongguanItem()
        #标题
        item['title'] = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract()[0] #if len(each.xpath("./td[2]/text()").extract()) > 0 else ''
        #先以空格做分割，取末尾，再以冒号做分割，再取末尾
        #编号
        item['number'] = item['title'].strip().split(' ')[-1].split(":")[-1]
        #图片
        img = response.xpath('//div[@class="textpic"]/img/@src')
        item['img'] = "http://wz.sun0769.com"+img[0] if len(img)>0 else " "
        content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
        # 内容
        item['content'] = "".join(content).replace("\xa0","")
        # 帖子链接
        item['url'] = response.url
        print(img)
        yield item
