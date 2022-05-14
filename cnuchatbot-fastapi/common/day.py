from datetime import datetime
from enum import Enum


class Day(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
    TODAY = datetime.today().weekday()

    def decode_kor_day(self):
        if self == "월요일":
            return Day.MONDAY.value
        elif self == "화요일":
            return Day.TUESDAY.value
        elif self == "수요일":
            return Day.WEDNESDAY.value
        elif self == "목요일":
            return Day.THURSDAY.value
        elif self == "금요일":
            return Day.FRIDAY.value
        elif self == "토요일":
            return Day.SATURDAY.value
        elif self == "일요일":
            return Day.SUNDAY.value