from datetime import date

vacation = date(2022, 6, 22)


def is_vacation():
    return date.today() >= vacation
