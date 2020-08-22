# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class ShowPipeline(object):

    def __init__(self):
        self.create_connection()
        #self.create_table()

    def create_connection(self):
        self.conxon = sqlite3.connect('dressage.db')
        self.cursr = self.conxon.cursor()
    
    # def create_table(self):
    #     self.cursr.execute("""DROP TABLE IF EXISTS show_results""")
    #     self.cursr.execute("""create table show_results(
    #             location text,
    #             event_type text,
    #             comp_title text,
    #             horse_id text,
    #             dob text,
    #             sex text,
    #             rider_id text,
    #             position text,
    #             score text
    #             )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursr.execute("""INSERT INTO show_results VALUES (?,?,?,?,?,?,?,?,?)""",(
            item['location'],
            item['event_type'],
            item['comp_title'],
            item['horse_id'],
            item['dob'],
            item['sex'],
            item['rider_id'],
            item['position'],
            item['score']
        ))
        self.conxon.commit()

class PedigreePipeline(object):

    def __init__(self):
        self.create_connection()
        #self.create_table()

    def create_connection(self):
        self.conxon = sqlite3.connect('dressage.db')
        self.cursr = self.conxon.cursor()

    # def create_table(self):
    #     self.cursr.execute("""DROP TABLE IF EXISTS pedigree""")
    #     self.cursr.execute("""CREATE TABLE pedigree(
    #             horse_id text,
    #             dam_ueln text,
    #             sire_ueln text,
    #             dam_id text,
    #             sire_id text,
    #             dob text,
    #             sex text,
    #             horse_ueln text
    #             )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursr.execute("""INSERT INTO pedigree VALUES (?,?,?,?,?,?,?,?)""",(
            item['horse_id'],
            item['dam_ueln'],
            item['sire_ueln'],
            None,
            None,
            item['dob'],
            item['sex'],
            item['horse_ueln']
        ))
        self.conxon.commit()