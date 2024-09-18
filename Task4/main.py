from module_for_check_date import _is_leap_year
from module_for_check_date import check_date
import datetime


def main():

    user_input = list(map(int, input("Введите дату для проверки: ").split('.')))
    date_user = user_input[0]
    month_user = user_input[1]
    year_user = user_input[2]

    print("Проверка на високосность года - ", _is_leap_year(year_user))
    # print(date_user)
    # print(month_user)
    # print(year_user)
    print("Проверка введеной даты на существование: ", check_date(date=date_user, month=month_user, year=year_user))
    print("Проверка даты через модуль 'datetime' - ", datetime.date(year_user, month_user, date_user))


if __name__ == '__main__':
    main()
