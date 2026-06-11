import scrapy

class OpenlibrarybooksSpider(scrapy.Spider):
    name = "openBooks"
    start_urls = [
        "https://openlibrary.org/search?q=data&mode=ebooks&has_fulltext=true"
    ]

    def parse(self, response):
        print("[My open library Books]")
        print(response.status)
        print(response.url)