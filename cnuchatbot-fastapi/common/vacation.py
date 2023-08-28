from datetime import date

vacation_start = date(2023, 6, 22)
vacation_end = date(2023, 9, 1)


def is_vacation():
    return vacation_start <= date.today() < vacation_end
