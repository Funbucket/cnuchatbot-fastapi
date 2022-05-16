import re
from operator import itemgetter

import requests
from bs4 import BeautifulSoup
from common.kakaoJsonFormat import *

GLOBAL_BASE_URL = "http://cnuint.cnu.ac.kr/cnuint/notice/"
GLOBAL_EVENT_URL = GLOBAL_BASE_URL +  "event.do"
GLOBAL_RECRUIT_URL = GLOBAL_BASE_URL +  "recruit.do"

# data parsing and make template
def make_global_response(list,title,baseUrl):
    row = list[0].find('a')
    href = itemgetter('href')(row)
    answer = list_card(title, row.get_text(strip=True), "자세히 보기", baseUrl + href)

    for i in range(1, 5):
        row = list[i].find("a")
        href = itemgetter('href')(row)

        a = make_item(row.get_text(strip=True), "자세히 보기" , baseUrl + href)
        answer['template']['outputs'][0]['listCard']['items'].append(a)
    return answer

# 국제교류본부 공지사항
def get_global_event():
    response = requests.get(GLOBAL_EVENT_URL)
    bs = BeautifulSoup(response.text,'html.parser')
    events = bs.find('table', attrs={'class': 'board-table'}).find_all('div',attrs={'class':'b-title-box'})

    return make_global_response(events,"국제교류본부 공지사항",GLOBAL_EVENT_URL)

# 국제교류본부 파견학생 모집
def get_global_recruit():
    response = requests.get(GLOBAL_RECRUIT_URL)
    bs = BeautifulSoup(response.text,'html.parser')
    recruits = bs.find('tbody').find_all('tr',attrs={'class':''})
    
    return make_global_response(recruits,"국제교류본부 파견학생 모집",GLOBAL_RECRUIT_URL)
