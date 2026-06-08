import scrapy

class BookSpider(scrapy.spider):
    name="books"
    # send request
    start_urls=["https://books.toscrape.com/"]
    # get Response
    def parse(self,response):
        print("This our response")
        print(response)