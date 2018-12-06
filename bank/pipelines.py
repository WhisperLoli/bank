# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd

class BankPipeline(object):
    """使用pipeline生成excel文件"""

    def __init__(self):
        self.list = list()

    def process_item(self, item, spider):
        self.list.append(dict(item))
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pd.DataFrame.from_records(data=self.list).to_excel("df_banks.xlsx",index=False)
