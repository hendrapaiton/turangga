import re
import scrapy

from turangga.items import TuranggaItem


class NamaSpider(scrapy.Spider):
    name = 'nama'
    allowed_domains = ['id.theasianparent.com']
    start_urls = [
        'https://id.theasianparent.com/nama-bayi-terinspirasi-dari-binatang']

    def parse(self, response, **kwargs):
        item = TuranggaItem()
        item['title'] = [re.sub(r'\d+\.\s*', '', v).replace(u'\xa0', '') for v in
                         response.xpath('//strong/text()').extract()
                         if v != "Artikel terkait:"][:-4]
        item['detail'] = [re.sub(u'(\u2018|\u2019)', ',', v).replace(u'\xa0', '')
                          for v in response.xpath('//p/text()').extract()][4:-19]
        yield item
