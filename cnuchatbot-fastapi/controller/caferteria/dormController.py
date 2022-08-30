import requests
from bs4 import BeautifulSoup

DORM_URL = "https://dorm.cnu.ac.kr/html/kr/sub03/sub03_0304.html"


def get_menu(day_num):
    """
    :return: breakfast, lunch, dinner menu lists
    """
    req = requests.get(DORM_URL)
    req.raise_for_status()
    soup = BeautifulSoup(req.content.decode('utf8', 'replace'), 'html.parser')
    trs = soup.find("table", attrs={"class": "default_view diet_table"}).find("tbody").find_all("tr")
    tds = trs[day_num].find_all("td")
    breakfast_raw_data, lunch_raw_data, dinner_raw_data = tds[1], tds[2], tds[3]

    breakfast_menu = process_data(breakfast_raw_data)
    lunch_menu = process_data(lunch_raw_data)
    dinner_menu = process_data(dinner_raw_data)

    return breakfast_menu, lunch_menu, dinner_menu


def process_data(menu_raw_data):
    menu = [i.strip() for i in menu_raw_data.find_all(text=True)]  # 글자로만 배열 생성
    menu = remove_english_menu(menu)  # 영어 메뉴 삭제
    menu = divide_by_type(menu)  # 메뉴 타입별 분리
    menu = list(filter(lambda x: len(x) > 0, menu))  # 없는 메뉴 자르기

    return menu


def remove_english_menu(menu):
    main_a_count = 0  # 메인A 반복 확인
    for i, m in enumerate(menu):
        if "메인A" in m or "MainA" in m:
            main_a_count += 1
            if main_a_count == 2:
                del menu[i-1:-1]
                return menu


def divide_by_type(menu):  # 메뉴 타입 별로 배열 분리: 최대 타입 개수 3개
    type_count = 0
    second_type_start = -1
    third_type_start = -1

    first_type_menu = []
    second_type_menu = []
    third_type_menu = []

    for i, m in enumerate(menu):
        if "메인" in m:
            type_count += 1
            if type_count == 2:
                second_type_start = i
            elif type_count == 3:
                third_type_start = i

    if third_type_start != -1:  # type 3개
        third_type_menu = menu[third_type_start:]
        if second_type_start != -1:
            second_type_menu = menu[second_type_start:third_type_start]
            first_type_menu = menu[0:second_type_start]
    elif second_type_start != -1:  # type 2개
        second_type_menu = menu[second_type_start:]
        first_type_menu = menu[0:second_type_start]
    else:  # type 1개
        first_type_menu = menu

    return first_type_menu, second_type_menu, third_type_menu


def get_str_menu(foods):
    ret = ""
    for f in foods:
        ret += f
        ret += "\n"
    return ret

