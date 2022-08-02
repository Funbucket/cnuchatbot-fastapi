from datetime import datetime

Day = {
    "MONDAY": 0,
    "TUESDAY": 1,
    "WEDNESDAY": 2,
    "THURSDAY": 3,
    "FRIDAY": 4,
    "SATURDAY": 5,
    "SUNDAY": 6,
    "TODAY": datetime.today().weekday()
}

def decode_kor_day(kor_day):
    if kor_day == "월요일":
        return Day["MONDAY"]
    elif kor_day == "화요일":
        return Day["TUESDAY"]
    elif kor_day == "수요일":
        return Day["WEDNESDAY"]
    elif kor_day == "목요일":
        return Day["THURSDAY"]
    elif kor_day == "금요일":
        return Day["FRIDAY"]
    elif kor_day == "토요일":
        return Day["SATURDAY"]
    elif kor_day == "일요일":
        return Day["SUNDAY"]

# today 자정 넘어가면 초기화되자않는 오류 해결책
def get_today():
    return datetime.today().weekday()