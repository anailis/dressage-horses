import scrapy
from ..items import Horse

# filepaths have been removed

ids_list = ['...']
links_list = ['...' + i for i in ids_list]
print(links_list)

class PedigreePedSpider(scrapy.Spider):
    name = "pedigree_ped"

    def start_requests(self):
        urls = links_list
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        horse_instance = Horse()
        try: 
            horse_instance['horse_ueln'] = str(response.xpath('/html/body/div[3]/div[2]/div[4]/div/svg/g/g[1]/text[5]/text()').extract()[0]).split()[2]
        except:
            horse_instance['horse_ueln'] = None
        try:
            horse_instance['horse_id'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/text()').extract()[0].strip()
        except:
            horse_instance['horse_id'] = None
        try: 
            horse_instance['dob'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/text()').extract()[0].strip()
        except:
            horse_instance['dob'] = None
        horse_instance['sex'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/text()').extract()[0].strip()
        try:
            horse_instance['sire_ueln'] = str(response.xpath('/html/body/div[3]/div[2]/div[4]/div/svg/g/g[2]/text[5]/text()').extract()[0]).split()[2]
        except:
            horse_instance['sire_ueln'] = None
        try:
            horse_instance['dam_ueln'] = str(response.xpath('/html/body/div[3]/div[2]/div[4]/div/svg/g/g[6]/text[5]/text()').extract()[0]).split()[2]
        except:
            horse_instance['dam_ueln'] = None
        yield horse_instance