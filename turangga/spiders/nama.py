import scrapy


class NamaSpider(scrapy.Spider):
    name = 'nama'
    allowed_domains = ['id.theasianparent.com']
    start_urls = ['https://id.theasianparent.com/nama-bayi-terinspirasi-dari-binatang']

    def parse(self, response, **kwargs):
        print('Response: ', response.xpath('//strong').get())
