from scrapy import Item, Field


class TuranggaItem(Item):
    title = Field()
    detail = Field()
