import scrapy 
from ..items import Show

# file paths have been removed

ids_list = ['...']

links_list = ['...' + i for i in ids_list]

class ShowResultsSpider(scrapy.Spider):
    name = "showresults"

    def start_requests(self):
        urls = links_list
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        show_instance = Show()
        table_xpath = '//*[@id="PlaceHolderMain_ucResult_gvcRes"]/tbody'
        table_length = len(response.xpath(table_xpath).xpath('.//tr').xpath('./td[1]/text()').extract()) + 1
        for i in range(3, table_length): 
            show_instance['horse_id'] = response.xpath('//*[@id="PlaceHolderMain_fvDetail"]/tbody/tr/td/div[2]/table/tbody/tr[2]/td[2]/text()').extract()[0].strip()
            show_instance['sex'] = response.xpath('//*[@id="PlaceHolderMain_fvDetail"]/tbody/tr/td/div[2]/table/tbody/tr[4]/td[2]/text()').extract()[0].strip()
            show_instance['dob'] = response.xpath('//*[@id="PlaceHolderMain_fvDetail"]/tbody/tr/td/div[2]/table/tbody/tr[3]/td[2]/text()').extract()[0].strip()
            show_instance['event_type'] = response.xpath(table_xpath).xpath('.//tr')[i].xpath('./td[4]/text()').extract()[0].strip()
            show_instance['location'] = response.xpath(table_xpath).xpath('.//tr')[i].xpath('./td[3]/text()').extract()[0].strip()
            show_instance['comp_title'] = response.xpath(table_xpath).xpath('.//tr')[i].xpath('./td[5]/a/text()').extract()[0].strip()
            show_instance['rider_id'] = response.xpath(table_xpath).xpath('.//tr')[i].xpath('./td[7]/a/text()').extract()[0].strip()
            try: 
                show_instance['position'] = response.xpath(table_xpath).xpath('.//tr')[i].xpath('./td[10]/span/text()').extract()[0].strip()
            except: 
                show_instance['position'] = None
            show_instance['score'] = response.xpath(table_xpath).xpath('.//tr')[i].xpath('./td[11]/text()').extract()[0].strip()
            yield show_instance
