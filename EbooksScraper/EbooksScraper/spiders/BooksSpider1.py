import scrapy
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

        print("")
    #     # Select all books
    #     print ("all books info")
    #     ebooks=response.css("article")
    #     for book in ebooks :
    #         title=book.css("a::text").get()
    #         print(title)
    #         price=book.css("p.price_color::text").get()
    #         print(price)
    #         availability=book.css("p.instock.availability").xpath("normalize-space()").get()
        
    #         print(availability)
    #         yield{
    #             "title":title,
    #             "price":price,
    #             "availability":availability,
               

    # }