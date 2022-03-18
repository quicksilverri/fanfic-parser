# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class FanficsPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_main_table()
        self.create_additional_tables('fandoms')
        self.create_additional_tables('parings')
        self.create_additional_tables('characters')
        self.create_additional_tables('warnings')
        self.create_additional_tables('freeforms')

    def create_connection(self):
        self.con = sqlite3.connect('fanfics.db')
        self.cur = self.con.cursor()

    def create_main_table(self):
        self.cur.execute('''DROP TABLE IF EXISTS main_info''')
        self.cur.execute('''
        CREATE TABLE main_info(
        fanfic_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT, 
        author TEXT,
        date TEXT,
        language TEXT,
        number_of_words INTEGER,
        hits INTEGER
        );
        ''')

    def create_additional_tables(self, type_of_info: str):
        '''Creates tables for additional tag-like information'''

        self.cur.execute(f'DROP TABLE IF EXISTS {type_of_info}')
        self.cur.execute(f'''
                CREATE TABLE {type_of_info}(
                {type_of_info}_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT UNIQUE
                );
                ''')

        self.cur.execute(f'''DROP TABLE IF EXISTS {type_of_info}_to_fanfics''')
        self.cur.execute(f'''CREATE TABLE {type_of_info}_to_fanfics(
                {type_of_info}_id INTEGER,
                fandom_id INTEGER,
                FOREIGN KEY (fandom_id) REFERENCES main_info (fanfic_id), 
                FOREIGN KEY ({type_of_info}_id) REFERENCES {type_of_info} ({type_of_info}_id)
                );
                ''')  

    def process_item(self, item, spider):
        self.store(item)
        return item

    def store(self, item):
        self.cur.execute('''INSERT INTO main_info VALUES (?, ?, ?, ?, ?, ?, ?)''', (
            item['title'],
            item['author'][0],
            item['date'][0],
            item['description'][0],
            item['language'][0],
            item['number_of_words'][0],
            item['hits'][0]
        ))
        self.con.commit()

    def store_additional_information(self, item, type_of_info: str):
        for piece in item[type_of_info]:
            try:
                self.cur.execute(f'''INSERT INTO {type_of_info} VALUES (?)''', piece)

        self.cur.execute(f'''INSERT INTO {type_of_info}_to_fanfics VALUES () ''')
        self.con.commit()




