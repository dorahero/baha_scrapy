import requests 
import random
import pymongo
from baha.util.mongo_setting import *

class ScyllaProxies(object):
    def __init__(self, number=50) -> None:
        url = f"http://127.0.0.1:8899/api/v1/proxies?limit={str(number)}"
        self.__number = number
        self.__proxies = requests.get(url).json().get("proxies")[:self.__number]        
    
    def __len__(self):
        return len(self.__proxies)

    def random_proxy(self):
        return ScyllaProxies.format(self.__proxies[random.randint(0,len(self.__proxies))])

    def to_list(self):
        return [ScyllaProxies.format_ip(f) for f in self.__proxies]
    
    def tolist(self):
        return [ScyllaProxies.format(f) for f in self.__proxies]
    
    @staticmethod
    def format(proxy_dict):
        ip=proxy_dict.get("ip")
        port=str(proxy_dict.get("port"))
        uri="https" if proxy_dict.get("is_https") else "http"
        return {uri:f"{uri}://{ip}:{port}/"}
    
    @staticmethod
    def format_ip(proxy_dict):
        ip=proxy_dict.get("ip")
        port=str(proxy_dict.get("port"))
        uri="https" if proxy_dict.get("is_https") else "http"
        return f"{uri}://{ip}:{port}/"

MONGODB_DB="scrapy"

class MongoProxies(object):
    def __init__(self, collection) -> None:
        connection = pymongo.MongoClient(
            host=MONGODB_HOST,
            port=MONGODB_PORT,
            username=MONGODB_USERNAME,
            password=MONGODB_PASSWORD
        )
        self.__collection=collection
        self.db=connection[MONGODB_DB]
        self.collection=self.db[collection]

    def get_all_data(self):
        return list(self.collection.find({}))

    def get_all_proxies(self):
        return [f.get("proxy") for f in self.collection.find({})]

if __name__=="__main__":
    a = MongoProxies("proxy_checked")
    print(a.get_all_proxies())

