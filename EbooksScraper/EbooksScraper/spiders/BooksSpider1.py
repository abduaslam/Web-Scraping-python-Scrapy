import scrapy
# import our Item class 
from EbooksScraper.items import booksItem
from EbooksScraper.items import Price_Int
from scrapy.loader import ItemLoader 
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
        # ##########################################################################
        print(["Thes Scrapy Without usig scrapy items "])
        # Select all books
        print ("all books info")
        ebooks=response.css("article")
        # for book in ebooks :
        #     title=book.css("a::text").get()
        #     print(title)
        #     price=book.css("p.price_color::text").get()
        #     availability=book.css("p.instock.availability").xpath("normalize-space()").get()
        #     yield {
        #         "title":title,
        #         "Price":price ,
        #          "availability" :availability          }
        # #######################################################################

        # create object from our Items
        bookitem=booksItem()
        # print(["Thes Scrapy Items "])
        # # Select all books
        # print ("all books info")
        # ebooks=response.css("article")
        # for book in ebooks :
        #     bookitem['title']=book.css("a::text").get()
        #     bookitem['price']=Price_Int(book.css("p.price_color::text").get())
        #     print(bookitem['price'])
        #     bookitem['availability']=book.css("p.instock.availability").xpath("normalize-space()").get()
        #     yield bookitem ;
            # #####################################################################
            #Loading Items with Scrapy ItemLoaders
        print("[Loading Items with Scrapy ItemLoaders]")   
        for book in ebooks :
            loader=ItemLoader(item=bookitem)
            loader.add_value('title',book.css("a::text").get())
            loader.add_value('price',(book.css("p.price_color::text").get()))
            loader.add_value('availability',book.css("p.instock.availability").xpath("normalize-space()").get())
            yield loader.load_item() ;

           
      