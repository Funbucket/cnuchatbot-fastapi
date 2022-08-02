from datetime import date

import requests
from bs4 import BeautifulSoup
from common.day import *


def encode_place(place):
    if place == "제2학생회관":
        return 2
    elif place == "제3학생회관":
        return 3
    elif place == "제4학생회관":
        return 4
    elif place == "생활과학대학":
        return 5


def decode_place(place_num):
    if place_num == 2:
        return "제2학생회관"
    elif place_num == 3:
        return "제3학생회관"
    elif place_num == 4:
        return "제4학생회관"
    elif place_num == 5:
        return "생활과학대학"


def get_hall_url(place_num):
    today = date.today().strftime("%Y.%m.%d")
    url = f"https://mobileadmin.cnu.ac.kr/food/index.jsp?searchYmd={today}&searchLang=OCL04.10&searchView=date&searchCafeteria=OCL03.0{place_num}&Language_gb=OCL04.10#tmp"
    return url


def get_menu(day_num, place_num):
    """
    :return: 0: 교직원아침, 1: 학생아침, 2: 교직원점심, 3: 학생점심
    """
    if day_num != 6:
        url = get_hall_url(place_num)
        req = requests.get(url)
        req.raise_for_status()
        soup = BeautifulSoup(req.content.decode('utf8', 'replace'), 'html.parser')
        table = soup.find("table", attrs={"class": "menu-tbl"})
        tbody = table.find("tbody")
        trs = tbody.find_all("tr")

        breakfast_faculty_raw_data = trs[0].find_all("td")
        breakfast_student_raw_data = trs[1].find_all("td")
        lunch_faculty_raw_data = trs[2].find_all("td")
        lunch_student_raw_data = trs[3].find_all("td")

        breakfast_faculty = process_data(breakfast_faculty_raw_data[day_num + 2])
        breakfast_student = process_data(breakfast_student_raw_data[day_num + 1])
        lunch_faculty = process_data(lunch_faculty_raw_data[day_num + 2])
        lunch_student = process_data(lunch_student_raw_data[day_num + 1])
    else:
        breakfast_faculty = ['운영안함']
        breakfast_student = ['운영안함']
        lunch_faculty = ['운영안함']
        lunch_student = ['운영안함']

    return breakfast_faculty, breakfast_student, lunch_faculty, lunch_student


def process_data(raw_data):
    menu = [i.strip() for i in raw_data.find_all(text=True)]  # 글자로만 배열 생성
    menu = list(filter(lambda x: x != '', menu))  # 공백 문자 제거
    return menu


def get_str_menu(foods):
    type_count = 0
    ret = ""
    for f in foods:
        if "정식" in f or "일품" in f:
            type_count += 1
            if type_count > 1:
                ret += "\n"
                ret += f
                ret += "\n"
            else:
                ret += f
                ret += "\n"
        else:
            ret += f
            ret += "\n"

    return ret

# test code
if __name__ == "__main__":
    utter = "토요일제2학생회관"
    kor_day = utter[:3]  # 월요일 ...
    place = utter[3:]  # 제2학생회관 ...
    print(get_menu(decode_kor_day(kor_day), encode_place(place)))
