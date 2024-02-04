# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AmazonSpiderTestPipeline:
     
    def open_spider(self, spider):
        self.lst = []

    def process_item(self, item, spider):
        data = {
            "url": item["url"],
            "title": item["title"],
            "price": item["price"],
            "img_product": item["img_product"],
            }

        self.lst.append(data)

        return item

    def close_spider(self, spider):

        print(self.lst, len(self.lst))

