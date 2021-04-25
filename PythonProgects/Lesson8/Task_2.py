class MyZeroDivisionException(Exception):
    def __init__(self, text):
        self.text = text


# Вариант 1
try:
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    if not b:
        raise MyZeroDivisionException("Вы обвиняетесь по делу 'Деление на ноль', вы имеете право хранить молчание!")
    print(f"a + b = {a / b}")
except (ValueError, MyZeroDivisionException) as error:
    print(error)


# Вариант 2
class MyNumber:
    def __init__(self, number):
        self.number = number

    def __floordiv__(self, other):
        if not other.number:
            raise MyZeroDivisionException("Вы обвиняетесь по делу 'Деление на ноль', вы имеете право хранить молчание!")
        return self.number // other.number

    def __truediv__(self, other):
        if not other.number:
            raise MyZeroDivisionException("Вы обвиняетесь по делу 'Деление на ноль', вы имеете право хранить молчание!")
        return self.number / other.number

    def __str__(self):
        return f"{self.number}"


number_1 = MyNumber(3)
number_2 = MyNumber(0)
try:
    print(number_1 / number_2)
    print(number_1 // number_2)
except MyZeroDivisionException as error:
    print(error)
