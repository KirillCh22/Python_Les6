

def _is_leap_year(year: int):
    return (year % 4 == 0)


def check_date(date: int, month: int, year: int):

    if date > 31:
        print("Ошибка, такой даты не существует, дата не может быть больше 31")
        return False
    elif date < 1:
        print("Ошибка, такой даты не существует, дата не может быть меньше 1")
        return False
    else:
        if month > 12:
            print("Ошибка, такого месяца не существует, месяц не может быть больше 12")
            return False
        elif month < 1:
            print("Ошибка, такого месяца не существует, месяц не может быть меньше 1")
            return False
        else:
            if year > 9999:
                print("Ошибка такого года не существует, год не может быть больше 9999")
                return False
            elif year < 1:
                print("Ошибка такого года не существует, год не может быть меньше 1")
                return False
            else:
                print("Такая  дата существует - {0}.{1}.{2}".format(date, month, year))
                return True
