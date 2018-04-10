# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AwsExamPipeline(object):
    def open_spider(self,spider):
        self.file = open('result.html','w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        html = '<h2>'+item['questions']+'</h2>'
        html = html + item['content']
        html = html+'<br>Answers:'+item['answers']+'<br>'*3
        self.file.write(html)
        return item