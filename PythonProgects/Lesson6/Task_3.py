class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position (Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(dict(self._income).values())


position_1 = Position("Василий", "Иванов", "Самый главный", {"wage": 25000, "bonus": 300})
print(f"Полное имя: {position_1.get_full_name()}")
print(f"Доход с учетом премии: {position_1.get_total_income()}")
