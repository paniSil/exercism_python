# checking if the year is a leap year


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and not year % 400 == 0:
            return False
        else:
            return True
    else:
        return False
