from openpyxl import workbook
from itemadapter import ItemAdapter


class EbooksscraperPipeline:
    def open_spider(self,spider):
        self.workbook=workbook()
        self.sheet=self.workbook.active()
        self.sheet.title="ebooks"
        self.sheet.append(spider.cols)
    def process_item(self, item, spider):
        pass
    def close_spider(self,spider):
        pass
