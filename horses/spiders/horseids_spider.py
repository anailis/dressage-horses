import scrapy


class HorseIDSpider(scrapy.Spider):
    name = "horseids"

    def start_requests(self):
        urls = [
            'http://webcache.googleusercontent.com/search?q=cache:https://data.fei.org/Ranking/Search.aspx?rankingCode=D_WR',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.xpath('//*[@id="PlaceHolderBottom_gvcResults"]/tr/td[position()=5]/a/@href').extract()
        with open("horselinks.txt", "a") as f:
            f.writelines(l + "\n" for l in links)
