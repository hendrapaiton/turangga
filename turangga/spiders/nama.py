import scrapy


class NamaSpider(scrapy.Spider):
    name = 'nama'
    allowed_domains = ['id.theasianparent.com']
    start_urls = ['http://id.theasianparent.com/']

    def parse(self, response):
        pass
