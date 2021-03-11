import requests
from bs4 import BeautifulSoup
import re
from baha.util.setting import HEADERS

def parse_reply_content(url):
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, 'html.parser')
    res = []
    for s in soup.select("div.cbox_msg2_list"):
        _ = {}
        pattern = re.compile(r'\d+')
        _['userid'] = pattern.findall(s['id'])[0]
        _['username'] = s.select("a")[0].text.replace("：", "")
        _['reply_time'] = s.select("span")[0].text
        _['post_good_point'] = s.select("button.gp")[0].text
        _['post_bad_point'] = s.select("button.bp")[0].text
        _['content'] = s.select("p")[0].text
        res.append(_)
    return res