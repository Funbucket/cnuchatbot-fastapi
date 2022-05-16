import re
from operator import itemgetter

import requests
from bs4 import BeautifulSoup
from common.kakaoJsonFormat import *

GLOBAL_BASE_URL = "http://cnuint.cnu.ac.kr/cnuint/notice/"
GLOBAL_EVENT_URL = GLOBAL_BASE_URL +  "event.do"
GLOBAL_RECRUIT_URL = GLOBAL_BASE_URL +  "recruit.do"
infoList = ["국제교류본부 알림","파견학생 모집"]

# 각종정보 홈 리플라이만 반환
def get_information_list():
    answer = ""
    answer = insert_text("보고싶은 정보를 클릭해주세요.")
    for label in infoList:
        reply = make_reply(label,label)
        answer = insert_replies(answer,reply)
    return answer


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
