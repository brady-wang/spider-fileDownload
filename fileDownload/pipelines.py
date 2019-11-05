# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import  FilesPipeline
class FiledownloadPipeline(object):
    def process_item(self, item, spider):
        tmp = item['file_urls']
        item['file_urls'] = []

        for i in tmp:
            if "?" in i:
                item['file_urls'].append(i.split('?')[0])
            else:
                item['file_urls'].append(i)
        return item


class  MyFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        file_path = request.url
        file_path = file_path.split('/')[-1]
        print("下载图片"+ file_path)
        return 'full/%s' % (file_path)