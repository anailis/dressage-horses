# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Horse(scrapy.Item):
    horse_id = scrapy.Field()
    horse_ueln = scrapy.Field()
    dam_ueln = scrapy.Field()
    sire_ueln = scrapy.Field()
    sire_id = scrapy.Field()
    dam_id = scrapy.Field()
    dob = scrapy.Field()
    sex = scrapy.Field()

class Show(scrapy.Item):
    location = scrapy.Field()
    event_type = scrapy.Field()
    comp_title = scrapy.Field()
    horse_id = scrapy.Field()
    dob = scrapy.Field()
    sex = scrapy.Field()
    rider_id = scrapy.Field()
    position = scrapy.Field()
    score = scrapy.Field()

    
