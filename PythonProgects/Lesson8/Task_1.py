class Date:
    __days_count_in_month = {1: 31, 2: (28, 29), 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30,
                             12: 31}

    def __init__(self, date):
        try:
            self.day, self.month, self.year = Date.__parse(date)
        except Exception as error:
            self.day, self.month, self.year = ["", "", ""]
            print(error)

    @staticmethod
    def __parse(date):
        date = str(date)
        if not date.count("-") == 2:
            raise ValueError(f"Incorrect date format '{date}', 'dd-mm-yyyy' required")

        date_values = [int(el) for el in date.strip().split("-") if el.isdigit()]
        if not len(date_values) == 3:
            raise ValueError(f"Incorrect date format '{date}', 'dd-mm-yyyy' required")

        day, month, year = date_values
        Date.__check_date_values(day, month, year)
        return date_values

    @classmethod
    def __check_date_values(cls, day, month, year):
        if year < 1 or year > 9999:
            raise ValueError(f"Year most be > 0 and < 9999")
        if month > 12 or month < 1:
            raise ValueError(f"Month most be > 1 and <= 12 ")

        if day < 1:
            raise ValueError(f"Day most be > 1")
        elif not month == 2 and day > cls.__days_count_in_month[month]:
            raise ValueError(f"Day most be <= {cls.__days_count_in_month[month]} ")
        elif month == 2:
            if not cls.__is_leap_year(year) and day > tuple(cls.__days_count_in_month[month])[0]:
                raise ValueError(f"Day most be <= {tuple(cls.__days_count_in_month[month])[0]}")
            elif day > tuple(cls.__days_count_in_month[month])[1]:
                raise ValueError(f"Day most be <= {tuple(cls.__days_count_in_month[month])[1]}")

    @staticmethod
    def __is_leap_year(year):
        annual_multiplicity_400 = year % 400
        annual_multiplicity_100 = year % 100
        annual_multiplicity_4 = year % 4

        return (annual_multiplicity_4 == 0 and annual_multiplicity_100 != 0) or annual_multiplicity_400 == 0

    def __str__(self):
        return "" if not self.day else f"{self.day}/{self.month}/{self.year}"


date_1 = Date("28-2-1991")
print(date_1)

date_2 = Date("29-2-1991")
print(date_2)
