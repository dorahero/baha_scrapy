# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import logging
from datetime import datetime

class BahaPipeline:
    collection_name = datetime.now().strftime("%Y%m%d")

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        ## initializing spider
        ## opening db connection
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        ## clean up when spider is closed
        self.client.close()

    def process_item(self, item, spider):
        ## how to handle each post
        data = dict(item).get("data")
        if 'information' in data:
            try:
                self.db[self.collection_name+"_info"].insert(data)
                logging.debug("Post added to MongoDB")
            except Exception:
                last_time = self.db[self.collection_name+"_info"].find_one({"_id" : data["_id"]})["insert_time"]
                NowDateTime = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")
                #calculate the difference
                timediff = datetime.strptime(NowDateTime, "%Y-%m-%dT%H:%M:%S") - datetime.strptime(last_time, "%Y-%m-%dT%H:%M:%S")
                
                #convert to seconds
                seconds = timediff.total_seconds()
                
                #Convert seconds to hours (there are 3600 seconds in an hour)
                hours = (timediff.seconds)/3600
                
                #Show the total
                if hours > 2:
                    self.db[self.collection_name+"_info"].update({"_id" : data["_id"]}, {"$set" : data})            
                    logging.debug("Post added to MongoDB")
            return item
        else:
            try:
                self.db[self.collection_name+"_"+data['title']].insert(data)
                logging.debug("Post added to MongoDB")
            except Exception:
                last_time = self.db[self.collection_name+"_"+data['title']].find_one({"_id" : data["_id"]})["insert_time"]
                NowDateTime = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")
                #calculate the difference
                timediff = datetime.strptime(NowDateTime, "%Y-%m-%dT%H:%M:%S") - datetime.strptime(last_time, "%Y-%m-%dT%H:%M:%S")
                
                #convert to seconds
                seconds = timediff.total_seconds()
                
                #Convert seconds to hours (there are 3600 seconds in an hour)
                hours = (timediff.seconds)/3600
                
                #Show the total
                if hours > 2:
                    self.db[self.collection_name+"_"+data['title']].update({"_id" : data["_id"]}, {"$set" : data})
                    logging.debug("Post added to MongoDB")
            return item