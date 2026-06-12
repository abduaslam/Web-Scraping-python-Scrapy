
from scrapy import Item,Field

class booksItem(Item):
    title=Field()
    price=Field()
    availability=Field()