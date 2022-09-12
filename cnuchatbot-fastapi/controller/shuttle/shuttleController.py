from common.data.shuttle.timeTable import *
from datetime import datetime, date, time, timedelta
from typing import NamedTuple
from common.kakaoJsonFormat import *
from common.holiday import is_holiday
from common.vacation import is_vacation

AVG_TIME = 20
CURRENT_TIME = datetime.now()
IMAGE_URL = {
   "A노선표": "https://res.cloudinary.com/dvrcr0hkb/image/upload/v1633810851/KakaoTalk_20210912_215636605_amglsv.jpg",
   "B노선표": "https://res.cloudinary.com/dvrcr0hkb/image/upload/v1633810851/KakaoTalk_20210904_200707497_hvhm8n.jpg",
   "C노선표": "https://res.cloudinary.com/dvrcr0hkb/image/upload/v1633810888/KakaoTalk_20211010_051327589_t0alks.jpg"
}

LINE_TIME = {
    "A": shuttle_a,
    "B": shuttle_b,
    "CB": shuttle_c_cb,  # 보운행
    "CD": shuttle_c_cd  # 대덕행
}


class AdjTimes(NamedTuple):
    """
    AdjTimes struct
    line_name : 노선명
    prev : 직전 차량 수
    next : 직후 차량 수
    times : 전, 후 차량 시간
    """
    line_name_: str
    prev_: int
    next_: int
    times_: list


def get_datetime(time):
    """
    get_datetime
    time object를 인자로 받아서
    오늘의 datetime object 반환
    """
    return datetime.combine(date.today(), time)


def get_str_time(time):
    """
    get_str_time
    time object를 인자로 받아서
    H:M 형식의 string 반환
    """
    return time.strftime("%H:%M")


def get_time_diff(x, y):
    """
    get_time_diff
    두개의 time object를 인자로 받아서
    차이값(절대값)을 분 단위로 반환한다.
    """
    return abs(int((get_datetime(x) - get_datetime(y)).total_seconds() / 60))


def is_running(time):
    """
    is_running
    time object를 인자로 받아서
    인자로 받은 시간의 차량이 현재 운행중인지 여부 반환
    """
    return get_datetime(time) < CURRENT_TIME < get_datetime(time) + timedelta(minutes=AVG_TIME)


def get_image(line):
    """
    get_line_image
    A노선표, B노선표, C노선표 중 하나를 인자로 받아서
    해당 노선 image를 kakao json format 로 반환
    """
    url = IMAGE_URL[line]
    answer = insert_image(url, line)
    answer = insert_multiple_reply(
        answer,
        [["A노선표", "A노선표"], ["B노선표", "B노선표"], ["C노선표", "C노선표"]]
    )
    return answer

def get_app_image():
    return [IMAGE_URL['A노선표'],IMAGE_URL['B노선표'],IMAGE_URL['C노선표'],IMAGE_URL['C노선표']]


def find_adjacent_times(line, cur_time):
    """
    find_adjacent_times
    노선의 이름(A, B)과 현재 시간을 인자로 받아서
    AdjTimes type을 반환한다.

    case 1 : 주말, 운행종료, 00시 이후 첫차 출발 30 분전 or 마지막 차량 30분 이후 24시 이전
    case 2 : 직전 0개 직후 2개, (첫차 - 30분) 이후 첫차 직전 (out of index 예외 처리)
    case 3 : 직전 1개 직후 2개, 첫차 출발 직후 두번째차 출발 직전 (out of index 예외 처리)

    case 4 : 대기중 0대, 운행중 0, 1, 2대
    case 5 : 대기중 1대, 운행중 0, 1, 2대
    case 6 : 대기중 2대, 운행중 0, 1, 2대
    """
    line_times = LINE_TIME[line]
    last_index = len(line_times) - 1

    # case 1
    if is_holiday() or get_datetime(time(0)) < cur_time < get_datetime(line_times[0]) - timedelta(minutes=30) or \
       get_datetime(line_times[last_index]) + timedelta(minutes=30) < cur_time < get_datetime(time(23, 59, 59)):
        return AdjTimes(line, 0, 0, [line_times[0], line_times[last_index]])

    # case 2
    elif get_datetime(line_times[0]) - timedelta(minutes=30) <= cur_time <= get_datetime(line_times[0]):
        return AdjTimes(line, 0, 2, [line_times[0], line_times[1]])

    # case 3
    elif get_datetime(line_times[0]) < cur_time <= get_datetime(line_times[1]):
        return AdjTimes(line, 1, 2, [line_times[0], line_times[1], line_times[2]])

    # case 4
    elif get_datetime(line_times[last_index]) < cur_time:
        # 운행중 2대, 대기중 0대
        if is_running(line_times[last_index - 1]):
            return AdjTimes(line, 2, 0, [line_times[last_index - 1], line_times[last_index]])
        # 운행중 1대, 대기중 0대
        elif is_running(line_times[last_index]):
            return AdjTimes(line, 1, 0, [line_times[last_index]])
        # 운행중 0대, 대기중 0대
        elif not is_running(line_times[last_index]):
            return AdjTimes(line, 0, 0, [line_times[0], line_times[last_index]])

    # case 5
    elif get_datetime(line_times[last_index - 1]) < cur_time <= get_datetime(line_times[last_index]):
        # 운행중 2대, 대기중 1대
        if is_running(line_times[last_index - 2]):
            return AdjTimes(line, 2, 1, [line_times[last_index - 2], line_times[last_index - 1], line_times[last_index]])
        # 운행중 1대, 대기중 1대
        elif is_running(line_times[last_index - 1]):
            return AdjTimes(line, 1, 1, [line_times[last_index - 1], line_times[last_index]])
        # 운행중 0대, 대기중 1대
        elif not is_running(line_times[last_index - 1]):
            return AdjTimes(line, 0, 1, [line_times[last_index - 1], line_times[last_index]])

    # case 6
    else:
        for index, val in line_times.items():
            # 운행중 2대, 대기중 2대
            if cur_time < get_datetime(val) and is_running(line_times[index - 2]):
                return AdjTimes(line, 2, 2, [line_times[index - 2], line_times[index - 1], line_times[index], line_times[index + 1]])
            # 운행중 1대, 대기중 2대
            elif cur_time < get_datetime(val) and is_running(line_times[index - 1]):
                return AdjTimes(line, 1, 2, [line_times[index - 1], line_times[index], line_times[index + 1]])
            # 운행중 0대, 대기중 2대
            elif cur_time < get_datetime(val) and not is_running(line_times[index - 1]):
                return AdjTimes(line, 0, 2, [line_times[index], line_times[index + 1]])


def get_str_info(adj_time, cur_time):
    """
    get_str_info
    AdjTimes struct와 current time을 인자로 받아서
    조건에 맞는 전, 후 차량의 시간을 string type으로 반환한다.
    """
    cur_time = cur_time.time()  # datetime object -> time object

    def get_info(prev, next):
        if prev == 0 and next == 0:
            info = "운행종료" + \
                   "\n첫차: " + get_str_time(adj_time.times_[0]) + " (월평역 출발)" + \
                   "\n막차: " + get_str_time(adj_time.times_[1])
        else:
            info = "[" + str(adj_time.prev_) + "대 운행중]"
            for i in range(prev):
                info += "\n" + get_str_time(adj_time.times_[i]) + "(" +str(get_time_diff(adj_time.times_[i], cur_time)) + "분전)"

            info += "\n\n"

            info += "[" + str(adj_time.next_) + "대 대기중]"
            for j in range(prev, prev + next):
                info += "\n" + get_str_time(adj_time.times_[j]) + "(" + str(get_time_diff(adj_time.times_[j], cur_time)) + "분전)"
        return info

    if is_vacation():
        ret = "방학 중 셔틀 운행 하지 않습니다."
    else:
        ret = get_info(adj_time.prev_, adj_time.next_)
    return ret


def get_time(isApp=False):
    """
    get_time
    get_str_info를 통해 얻은 각 노선의 정보
    kakao json format으로 반환한다.
    views에서 최종적으로 사용된다.
    """
    global CURRENT_TIME
    CURRENT_TIME = datetime.now()

    # a노선
    a = find_adjacent_times("A", CURRENT_TIME)
    a_str_info = get_str_info(a, CURRENT_TIME)
    answer = carousel_basic_card(a.line_name_ + "노선(순환)", a_str_info)

    # b노선
    b = find_adjacent_times("B", CURRENT_TIME)
    b_str_info = get_str_info(b, CURRENT_TIME)
    answer = insert_carousel_item(answer, b.line_name_ + "노선(순환)", b_str_info)
    
    # c노선
    if is_vacation():
        ret = "방학 중 셔틀 운행 하지 않습니다."
        answer = insert_carousel_item(answer, "C노선(보운행)", ret)
        answer = insert_carousel_item(answer, "C노선(대덕행)", ret)
    else:
        # c노선 보운행
        cb_str = ""
        for t in LINE_TIME["CB"].values():
            cb_str += get_str_time(t)
            cb_str += "\n"

        answer = insert_carousel_item(answer, "C노선(보운행)", cb_str)

        # c노선 대덕행
        cd_str = ""
        for t in LINE_TIME["CD"].values():
            cd_str += get_str_time(t)
            cd_str += "\n"
        
        if(isApp):
            return (a_str_info,b_str_info,cb_str,cd_str);
        answer = insert_carousel_item(answer, "C노선(대덕행)", cd_str)

        # 노선표 replies 추가
        answer = insert_multiple_reply(
            answer,
            [["A노선표", "A노선표"], ["B노선표", "B노선표"], ["C노선표", "C노선표"]]
        )

    return answer


if __name__ == "__main__":
    print(get_time())