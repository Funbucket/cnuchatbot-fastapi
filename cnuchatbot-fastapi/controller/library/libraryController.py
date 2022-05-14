import re
import requests
from bs4 import BeautifulSoup

from common.data.library.timeTable import *
from common.kakaoJsonFormat import *
from common.vacation import is_vacation

LIBRARY_URL = "https://clicker.cnu.ac.kr/Clicker/k/"
LIBRARY_TIME_URL = "https://library.cnu.ac.kr/webcontent/info/48"
LIBRARY_IMAGE_URL = "https://library.cnu.ac.kr/image/ko/local/guide/floor"
FLOORS = ["B2층", "B1층", "별관1층", "1층", "2층", "3층", "4층", "5층"]


def get_crawled_data():
    url = LIBRARY_URL
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    tds = soup.find("tbody").find_all("td", attrs={"class": re.compile("^clicker")})
    data = [i.get_text().strip() for i in tds]
    return data


def library_json_format_total():
    data = get_crawled_data()
    # value 값
    value = []
    for i in range(11):
        value.append("잔여좌석:" + data[4 * i + 2])

    # dict 생성
    library_info = {}
    for i in range(11):
        library_info[data[4 * i]] = value[i]
    return library_info


def get_library_seats():
    name = []
    library_info = library_json_format_total()
    answer = ""

    for key in library_info:
        answer += "\n" + "[" + key + "]" + "\n" + library_info[key] + "\n"
        name.append(key)
    answer = insert_text(answer)
    reply = make_reply("층별지도보기", "층별지도보기")
    answer = insert_replies(answer, reply)

    return answer


def get_library_image():
    for i, floor in enumerate(FLOORS):
        if floor == "별관1층":
            n = int(floor[2]) - 1  # library.cnu.ac.kr/image/ko/local/guide/floor0.png
        else:
            n = floor[:-1]
        url = f"{LIBRARY_IMAGE_URL}{n}.png"
        if i != 0:
            answer = insert_carousel_item(answer, floor, "")
            answer = insert_carousel_image(answer, url)
            answer = insert_carousel_button(answer, "자세히", url)
        else:  # 첫 번째 carousel 선언
            answer = carousel_basic_card(floor, "")
            answer = insert_carousel_image(answer, url)
            answer = insert_carousel_button(answer, "자세히", url)

    answer = insert_multiple_reply(answer, [["열람실 좌석보기", "열람실좌석현황"]])
    return answer


def get_str_time(type):
    """
    :param type: 자료실, 열람실, 크리에티브존
    """
    ret = ""
    for t in type:
        ret += "[" + t + "]"
        ret += "\n"
        if is_vacation():  # 방학중
            for w in type[t]["vacation"]:
                week = "주말" if w == "weekend" else "평일"
                if type[t]["vacation"][w] == "24시간 운영":
                    ret += f"{week}: 24시간운영"
                elif type[t]["vacation"][w] == "미운영":
                    ret += f"{week}: 미운영"
                else:
                    open_time = type[t]["vacation"][w]["open"].strftime("%H:%M")[1:]
                    close_time = type[t]["vacation"][w]["close"].strftime("%H:%M")
                    ret += f"{week}: {open_time}~{close_time}"
        else:  # 학기중
            for w in type[t]["semester"]:
                week = "주말" if w == "weekend" else "평일"
                if type[t]["semester"][w] == "24시간 운영":
                    ret += f"{week}: 24시간운영"
                elif type[t]["semester"][w] == "미운영":
                    ret += f"{week}: 미운영"
                else:
                    open_time = type[t]["semester"][w]["open"].strftime("%H:%M")[1:]
                    close_time = type[t]["semester"][w]["close"].strftime("%H:%M")
                    ret += f"{week}: {open_time} ~ {close_time}"
                ret += "\n"
        ret += "\n"
    return ret


def get_library_time():
    # 자료실
    answer = carousel_basic_card("자료실", get_str_time(reference_room))
    answer = insert_carousel_button(answer, "자세히", LIBRARY_TIME_URL)

    # 열람실
    answer = insert_carousel_item(answer, "열람실", get_str_time(reading_room))
    answer = insert_carousel_button(answer, "자세히", LIBRARY_TIME_URL)

    # 크리에이티브존
    answer = insert_carousel_item(answer, "크리에이티브존", get_str_time(creative_zone))
    answer = insert_carousel_button(answer, "자세히", LIBRARY_TIME_URL)

    answer = insert_multiple_reply(
        answer,
        [["열람실 좌석현황", "열람실좌석현황"], ["층별지도보기", "층별지도보기"]]
    )

    return answer


if __name__ == "__main__":
    print(get_library_time())
