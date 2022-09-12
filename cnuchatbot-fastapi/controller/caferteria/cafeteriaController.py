from common.data.cafeteria.timeTable import *
from common.kakaoJsonFormat import *
from controller.caferteria import dormController as Dorm
from controller.caferteria import hallController as Hall

STUDENT_1_IMAGE_URL = "https://cnuit.cnu.ac.kr/patis/system/ReportImageViewController.do?platformType=exbuilder&method=view&f0=cooperation&f1=consumer&f2=ocl02&f3=20220509&f4=C87EB9495CF142EFB831F158D3B64390.jpg"


def get_str_type(t):
    if t == "breakfast":
        ret = "아침"
    elif t == "lunch":
        ret = "점심"
    else:
        ret = "저녁"
    return ret


def get_str_time(place):
    """
    :param place: dormitory, student_1, student_2, student_3, student_4, domestic_science
    """
    ret = ""

    if place == "미운영":  # 미운영
        ret += "미운영"
    else:  # 나머지 식당 (기숙사식당, 2,3,4학생식당)
        for t in place:  # t = breakfast or lunch or dinner
            ret += f"[{get_str_type(t)}]"
            ret += "\n"
            for w in place[t]:  # w = weekday or weekend
                week = "주말" if w == "weekend" else "평일"
                if place[t][w] == "미운영":
                    ret += f"{week}: 미운영"
                else:
                    open_time = place[t][w]["open"].strftime("%H:%M")
                    close_time = place[t][w]["close"].strftime("%H:%M")
                    ret += f"{week}: {open_time}~{close_time}"
                ret += "\n"
            ret += "\n"
    return ret


def get_cafeteria_time():

    # 기숙사
    answer = carousel_basic_card("기숙사", get_str_time(dormitory))

    # 제1학생회관
    answer = insert_carousel_item(answer, "제1학생회관", "")
    answer = insert_carousel_image(answer, STUDENT_1_IMAGE_URL)
    answer = insert_carousel_button(answer, "자세히", STUDENT_1_IMAGE_URL)

    # 제2학생회관
    answer = insert_carousel_item(answer, "제2학생회관", get_str_time(student_2))

    # 제3학생회관
    answer = insert_carousel_item(answer, "제3학생회관", get_str_time(student_3))

    # 제4학생회관
    answer = insert_carousel_item(answer, "제4학생회관", get_str_time(student_4))

    # 생활과학대학
    answer = insert_carousel_item(answer, "생활과학대학", get_str_time(domestic_science))

    answer = insert_multiple_reply(
        answer,
        [["기숙사", "기숙사"], ["제2학생회관", "제2학생회관"], ["제3학생회관", "제3학생회관"],
         ["제4학생회관", "제4학생회관"], ["생활과학대학", "생활과학대학"]]
    )

    return answer

def get_app_cafeteria_time():
    cafeteria_time_info = {}
    cafeteria_time_info["기숙사"] = get_str_time(dormitory)
    cafeteria_time_info["제1학생회관"] = "라면&간식&양식\n10:00~14:00\n17:30~19:00\n스낵&한식&일식&중식\n11:00~14:00\n*주말,공휴일 운영안함"
    cafeteria_time_info["제2학생회관"] = get_str_time(student_2)
    cafeteria_time_info["제3학생회관"] = get_str_time(student_3)
    cafeteria_time_info["제4학생회관"] = get_str_time(student_4)
    cafeteria_time_info["생활과학대학"] = get_str_time(domestic_science)

    return cafeteria_time_info



def get_dorm_menu(day_num):
    menu = Dorm.get_menu(day_num)

    for i, m in enumerate(menu):
        if i == 0:  # 아침
            time = "아침"
            for k, t in enumerate(m):
                if k != 0:
                    answer = insert_carousel_item(answer, time, Dorm.get_str_menu(t), -1)
                else:  # 첫 번째 carousel 선언
                    answer = carousel_basic_card(time, Dorm.get_str_menu(t))
        elif i == 1:  # 점심
            time = "점심"
            for k, t in enumerate(m):
                if k != 0:  # 최신 output 에 추가된 carousel 에 추가
                    answer = insert_carousel_item(answer, time, Dorm.get_str_menu(t), -1)
                else:  # 새로운 carousel output 추가
                    answer = insert_carousel_output(answer, time, Dorm.get_str_menu(t))
        else:  # 저녁
            time = "저녁"
            for k, t in enumerate(m):
                if k != 0:
                    answer = insert_carousel_item(answer, time, Dorm.get_str_menu(t), -1)
                else:
                    answer = insert_carousel_output(answer, time, Dorm.get_str_menu(t))

    answer = insert_multiple_reply(answer, [["월", "월요일기숙사"], ["화", "화요일기숙사"], ["수", "수요일기숙사"], ["목", "목요일기숙사"], ["금", "금요일기숙사"], ["토", "토요일기숙사"], ["일", "일요일기숙사"]])
    return answer


def get_hall_menu(day_num, place):
    menu = Hall.get_menu(day_num, place)

    for i, m in enumerate(menu[:2]):
        time = "아침"
        if i == 0:
            answer = carousel_basic_card(time, f"[직원]\n{Hall.get_str_menu(m)}")
        else:
            answer = insert_carousel_item(answer, time, f"[학생]\n{Hall.get_str_menu(m)}")

    for i, m in enumerate(menu[2:]):
        time = "점심"
        if i == 0:
            answer = insert_carousel_output(answer, time, f"[직원]\n{Hall.get_str_menu(m)}")
        else:
            answer = insert_carousel_item(answer, time, f"[학생]\n{Hall.get_str_menu(m)}", -1)

    place = Hall.decode_place(place)
    answer = insert_multiple_reply(answer, [["월", f"월요일{place}"], ["화", f"화요일{place}"], ["수", f"수요일{place}"], ["목", f"목요일{place}"], ["금", f"금요일{place}"]])

    return answer


if __name__ == "__main__":
    get_dorm_menu(0)
