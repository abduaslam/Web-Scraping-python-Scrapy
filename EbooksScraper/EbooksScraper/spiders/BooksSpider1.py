import scrapy
# import our Item class 
from EbooksScraper.items import booksItem
# Create spider
class BookSpider(scrapy.Spider):
    name="books"
    # send request
    start_urls=["https://books.toscrape.com/"]
    # get Response
    def parse(self,response):

        print("This our response")
        # use css selector(Tag name)

        print(response.css("h3 a::text").get())
        # xpath selector
        print("[Xpath Selector]")
        print("tag name:",response.xpath("//h3/a/text()").get())
        print("Atrribute:",response.xpath("//p[@class='price_color']/text()").get())
        print("avialbility :", response.xpath("//p[@class='instock availability']/text()").get())

        # create object from our Items
        bookitem=booksItem()
        # Select all books
        print ("all books info")
        ebooks=response.css("article")
        for book in ebooks :
            bookitem['title']=book.css("a::text").get()
            bookitem['price']=book.css("p.price_color::text").get()
            bookitem['availability']=book.css("p.instock.availability").xpath("normalize-space()").get()
            yield bookitem ;