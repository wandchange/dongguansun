# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json

class DongguanPipeline(object):
    # __init__方法是可选的，作为类的初始化方法
    def __init__(self):
        # 创建了一个文件对象
        self.filename = open("dongguan.json", "wb")

    # process_item方法是必须写的，用来处理item数据
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(jsontext.encode("utf-8"))
        # json.dump(dict(item),self.filename)
        return item

    # close_spider方法是可选的，结束时调用此方法
    def close_spider(self, spider):
        self.filename.close()
