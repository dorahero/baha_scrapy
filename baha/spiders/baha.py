from baha.items import BahaItem
from baha.util.setting import *
from bs4 import BeautifulSoup
import scrapy
import time
import re
from datetime import datetime
from baha.utils import ScyllaProxies, MongoProxies
# from baha.util.proxy_list import PROXY_LIST
# import random
import requests
from baha.model.method import parse_reply_content

class BahaSpider(scrapy.Spider):
    name:str = "baha"
    NowDateTime = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")         
    headers = HEADERS
    domain = "http://forum.gamer.com.tw/"
    def start_requests(self):        
        for i in range(TITLE_PAGE):
            url = f'http://forum.gamer.com.tw/ajax/rank.php?c=21&page={i+1}'
            
            yield scrapy.Request(url=url, callback=self.parse_title)

    def parse_title(self, response):           
        json_data = response.json()        
        item = BahaItem()
        for j in json_data:
            res = {}
            _ = {}
            title = j['title']
            _['title'] = title
            _['hot'] = j['hot']
            _['ranking'] = j['ranking']
            bsn = j['bsn']
            res['_id'] = bsn
            res['information'] = _
            res["insert_time"] = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")     
            
            item['data'] = res
            yield item
            for p in range(ARTICLE_PAGE):
                # url = f'http://forum.gamer.com.tw/B.php?page={p+1}&bsn={bsn}'
                url = f'https://m.gamer.com.tw/ajax/MB_B_2k14.php?bsn={bsn}&subbsn=0&ltype=&page={p+1}&keyword='
                yield scrapy.Request(url=url, cb_kwargs={"title": title, "bsn": bsn}, callback=self.parse_article_title)

    def parse_article_title(self, response, title, bsn):
        soup = BeautifulSoup(response.body)
        for s in soup.select("li"):
            res = {}
            res["title"] = title
            # try:
            # with open('_.html', 'w', encoding='utf-8') as f:
            #     f.write(str(s.select("a")[0]))
            try:
                check = s.select("a")
                if check:
                    _ = s.select("a")[0]
                    snA = _["id"].replace("snA_", "")
                    category = s.select("p.blist1")[0].text[:2] # category
                    res["category"] = category
                    artitcle_title = s.select("h4")[0].text # title
                    res["artitcle_title"] = artitcle_title
                    try: update_time = s.select("p.blist2 span")[0].text 
                    except Exception: update_time = "X"
                    res["update_time"]  = update_time
                    reply_num = s.select("p.blist2")[0].text.replace(update_time, "")
                    res["reply_num"] = reply_num
                    res["_id"] = str(snA)+str(bsn)
                    res["bsn"] = str(bsn)
                    url = f"https://m.gamer.com.tw/forum/C.php?bsn={bsn}&snA={snA}&bpage=1&ltype="
                    res["article_url"] = url
                    yield scrapy.Request(url=url, meta={"res": res}, callback=self.parse_article_content)   
            except Exception as e:
                print(e)

    def parse_article_content(self, response):
        res = response.meta['res']
        soup = BeautifulSoup(response.body)
        content = []
        item = BahaItem()
        bsn = res['bsn']
        for s in soup.select("div.cbox"):
            try:
                if s.select("article.cbox_txt")[0]:
                    _ = {}
                    user_info = s.select("div.cbox_man span")
                    _['userid'], username = user_info[0].text.split(" ")
                    matchobj = re.compile(r"[(](.*?)[)]")
                    match = matchobj.search(username)
                    _['username'] = match.group(1)
                    _['floor'] = user_info[1].text
                    _['post_good_point'] = s.select("div.c-gp span.gp-count")[0].text
                    _['post_bad_point'] = s.select("div.c-bp span.gp-count")[0].text
                    _['post_time'] = user_info[-1].text
                    _["post_content"] = s.select("article.cbox_txt")[0].text
                    pattern = re.compile(r'\d+')
                    _['reply_id'] = pattern.findall(s.select("article.cbox_txt")[0]["id"])[0]
                    reply_content_id = pattern.findall(s.select("section.cbox_msg2 div")[0]["id"])[0]
                    _['reply_content_id'] = reply_content_id
                    url = f'https://m.gamer.com.tw/ajax/MB_forum_commend_all.php?bsn={bsn}&snB={reply_content_id}'
                    reply_content_content = parse_reply_content(url)
                    _['reply_content_content'] = reply_content_content
                    content.append(_)
            except Exception as e:
                print(e)
        res["content"] = content
        res["insert_time"] = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")     
        item['data'] = res
        # url = ""
        # yield scrapy.Request(url=url, meta={"res": res}, callback=self.parse_reply_content)
        yield item