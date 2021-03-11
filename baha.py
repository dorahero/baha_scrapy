import requests
import json
import os
from bs4 import BeautifulSoup
import time
import re
# from urllib.parse import urlparse

cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")
cop2 = re.compile("[^\u4e00-\u9fa5^0-9]")

# for i in range(10):
#     url = f'https://forum.gamer.com.tw/ajax/rank.php?c=21&page={i+1}'
#     print(url)
# url = 'https://forum.gamer.com.tw/ajax/rank.php?c=21&page=1'
# s = '''user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'''
# headers = {r.split(': ')[0]: r.split(': ')[1] for r in s.split('\n')}
# domain = "https://forum.gamer.com.tw/B.php?page=1&bsn=38144"
# res = requests.get(url, headers=headers)
# json_data = json.loads(res.text)
# res = json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')
# print(res.decode())
# for i in range(10):
#     url = f'https://forum.gamer.com.tw/B.php?page={i+1}&bsn=60076'
#     s = '''user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'''
#     headers = {r.split(': ')[0]: r.split(': ')[1] for r in s.split('\n')}
#     domain = "https://forum.gamer.com.tw/B.php?page=1&bsn=38144"
#     res = requests.get(url, headers=headers)
#     # json_data = json.loads(res.text)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     for s in soup.select("tr.b-list__row"):
#         # for x in s.select("td.b-list__summary"):
#         #     print(x.select('a')[0]['name'])
#         #     print(x.select('a')[1].text)
#         #     print(x.select('span.b-list__summary__gp')[0].text)
#         for ss in s.select("td.b-list__main div.b-list__tile p.b-list__main__title"):
#             print(ss.text)
    # try:
    #     print(s['name'])
    # except Exception as e:
    #     print(s.text)
# with open('_.html', 'w', encoding='utf-8') as f:
#     f.write(str(soup))
# for i in range(10):
#     url = f'https://m.gamer.com.tw/ajax/MB_B_2k14.php?bsn=60076&subbsn=0&ltype=&page=2&keyword='
#     url = re.sub(r"amp;", "", url)
#     s = '''user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'''
#     headers = {r.split(': ')[0]: r.split(': ')[1] for r in s.split('\n')}
#     # domain = "https://forum.gamer.com.tw/B.php?page=1&bsn=38144"
#     res = requests.get(url, headers=headers)
#     # json_data = json.loads(res.text)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     # print(soup)
#     with open('_.html', 'w', encoding='utf-8') as f:
#         f.write(str(soup))
#     for s in soup.select("li"):
#         try:
#             _ = s.select("a")[0]
#             matchobj = re.compile(r"[(](.*?)[)]")
#             match = matchobj.search(_["onclick"])
#             ariticle_id = match.group(1)
#             print(ariticle_id)
#             print(s.select("p.blist1")[0].text[:2]) # category
#             print(s.select("p.blist1")[0].text[2:]) # hot
#             print(s.select("h4")[0].text) # title
#         except Exception:
#             continue
#     # s = soup.select('div[class="c-section__main c-post"]')
#     break
    # for i in s:
    #     print(i.select("div.c-post__header__author a.floor")[0].text)
    #     print(i.select("div.c-post__header__author a.username")[0].text)
    #     print(i.select("div.c-post__header__author a.userid")[0].text)
    #     print(i.select("div.postcount span.postgp")[0].text)
    #     print(i.select("div.postcount span.postbp")[0].text)
    #     print(i.select('div.c-post__header__info a[class="edittime tippy-post-info"]')[0].text)
    #     print(i.select('div.c-post__body div.c-article__content')[0].text)
# with open('_.html', 'w', encoding='utf-8') as f:
#     f.write(str(soup))
for i in range(10):
    url = f'https://m.gamer.com.tw/ajax/MB_forum_commend_all.php?bsn=36833&snB=72605'
    # url = re.sub(r"amp;", "", url)
    s = '''user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'''
    headers = {r.split(': ')[0]: r.split(': ')[1] for r in s.split('\n')}
    # domain = "https://forum.gamer.com.tw/B.php?page=1&bsn=38144"
    res = requests.get(url, headers=headers)
    # json_data = json.loads(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    for s in soup.select("div.cbox_msg2_list"):
        _ = {}
        pattern = re.compile(r'\d+')
        _['userid'] = pattern.findall(s['id'])[0]
        _['username'] = s.select("a")[0].text.replace("：", "")
        _['reply_time'] = s.select("span")[0].text
        _['post_good_point'] = s.select("button.gp")[0].text
        _['post_bad_point'] = s.select("button.bp")[0].text
        _['content'] = s.select("p")[0].text
        print(_)
# for i in range(10):
#     url = f'https://m.gamer.com.tw/ajax/MB_forum_commend_all.php?bsn=23805&snB=3859599'
#     url = re.sub(r"amp;", "", url)
#     s = '''user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'''
#     headers = {r.split(': ')[0]: r.split(': ')[1] for r in s.split('\n')}
#     # domain = "https://forum.gamer.com.tw/B.php?page=1&bsn=38144"
#     res = requests.get(url, headers=headers)
#     # json_data = json.loads(res.text)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     print(soup)
#     with open('_.html', 'w', encoding='utf-8') as f:
#         f.write(str(soup))
#     # s = soup.select('div[class="c-section__main c-post"]')
#     break