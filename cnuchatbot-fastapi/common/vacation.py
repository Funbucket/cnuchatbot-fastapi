from datetime import date

vacation_start = date(2022, 12, 21)
vacation_end = date(2023, 3, 1)


def is_vacation():
    return vacation_start <= date.today() < vacation_end
