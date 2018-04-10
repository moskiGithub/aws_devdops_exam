import scrapy
from aws_exam.items import AwsExamItem


class examScapy(scrapy.Spider):
    name = "aws_exam"
    start_urls = ["http://www.briefmenow.org/amazon/which-of-the-following-approaches-given-this-company/"]

    def parse(self, response):
        examItem = AwsExamItem()

        items = response.xpath('//div[@class="entry-content"]/p')
        examItem['questions'] = ' '.join(items[0].xpath('.//text()').extract())
        items.pop(0)
        for item in items:
            data = ' '.join(item.xpath('.//text()').extract())
            if examItem.get('content') == None:
                examItem['content'] =data.strip()
                continue
            examItem['content']=examItem['content']+'<br>'+ data.strip()
        for item in  response.xpath('//div[@class="entry-content"]/p[@class="rightAnswer"]'):
            data = item.xpath('.//text()').extract_first()
            if examItem.get('answers',None) is None:
                examItem['answers'] = data.strip()
                continue
            examItem['answers']=examItem['answers']+ data.strip()

        yield examItem

        next_path = response.xpath('//div[@class="nav-next"]/a/@href').extract_first()
        if next_path is not None:
            yield scrapy.Request(next_path, callback=self.parse)
