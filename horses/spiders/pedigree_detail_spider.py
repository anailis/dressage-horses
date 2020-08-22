import scrapy
from ..items import Horse

# filepaths have been removed

ids_list = ['...']
links_list = ['...' + i for i in ids_list]

class PedigreeDetailSpider(scrapy.Spider):
    name = "pedigree_detail"

    def start_requests(self):
        urls = links_list
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        horse_instance = Horse()
        horse_instance['horse_id'] = response.xpath('//div[@id="PlaceHolderMain_fvDetail_panIDAndPassport"]//div[@class="formleft"]//tbody[1]/tr[1]/td[2]/text()').extract()[0].strip()
        horse_instance['dob'] = response.xpath('//div[@id="PlaceHolderMain_fvDetail_panHorseInfo"]//div[@class="formleft"]//tbody//tr[2]/td[2]/div[1]/text()').extract()[0].strip()
        horse_instance['sex'] = response.xpath('//div[@id="PlaceHolderMain_fvDetail_panHorseInfo"]//div[@class="formleft"]//tbody//tr[8]/td[2]/text()').extract()[0].strip()
        horse_instance['horse_ueln'] = response.xpath('//*[@id="PlaceHolderMain_fvDetail_panIDAndPassport"]/div[1]/table/tbody/tr[6]/td[2]/text()').extract()[0].strip()
        try:
            horse_instance['sire_ueln'] = response.xpath('//*[@id="PlaceHolderMain_fvDetail_lblSireUELN"]/text()').extract()[0].strip()
        except:
            horse_instance['sire_ueln'] = None
        try:
            horse_instance['dam_ueln'] = response.xpath('//*[@id="PlaceHolderMain_fvDetail_lblDamUELN"]/text()').extract()[0].strip()
        except:
            horse_instance['dam_ueln'] = None
        with open('parentlinks.txt', 'a') as f:
            try: 
                print(response.xpath('//a[@id="PlaceHolderMain_fvDetail_hlSire"]/@href').extract()[0], file=f)
            except:
                pass
            try:
                print(response.xpath('//a[@id="PlaceHolderMain_fvDetail_hlDam"]/@href').extract()[0], file=f)
            except:
                pass
        yield horse_instance 
