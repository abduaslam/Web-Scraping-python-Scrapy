
from scrapy import Item,Field
from itemloaders.processors import MapCompose,TakeFirst
def Price_Int(text):
    return float(text.replace('£',''))
class booksItem(Item):
    title=Field()
    price=Field(
        input_processer=MapCompose(Price_Int),
        output_processer=TakeFirst()
    )
    availability=Field()