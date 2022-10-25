import scrapy

from turangga.items import TuranggaItem


class NamaSpider(scrapy.Spider):
    name = 'nama'
    allowed_domains = ['id.theasianparent.com']
    start_urls = ['https://id.theasianparent.com/nama-bayi-terinspirasi-dari-binatang']

    def parse(self, response, **kwargs):
        item = TuranggaItem()
        item['title'] = [v for v in response.xpath('//strong/text()') if v.get() != "Artikel terkait:"][:-4]
        item['detail'] = response.xpath('//p/text()')[4:-19]
        yield item
