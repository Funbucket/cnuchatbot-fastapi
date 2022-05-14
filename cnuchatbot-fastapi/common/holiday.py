from pytimekr import pytimekr
from datetime import date, datetime
import datetime


def is_holiday():
    holiday_list = pytimekr.holidays()
    ret = False
    week_no = datetime.datetime.today().weekday()
    for holiday in holiday_list:
        if holiday == date.today() or week_no > 4:
            ret = True
        else:
            pass
    return ret
