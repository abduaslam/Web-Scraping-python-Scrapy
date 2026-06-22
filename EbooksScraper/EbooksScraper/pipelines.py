from openpyxl import workbook
from itemadapter import ItemAdapter


class EbooksscraperPipeline:
    def open_spider(self,spider):
        pass
    def process_item(self, item, spider):
        return item
    def close_spider(self,spier):
        pass
