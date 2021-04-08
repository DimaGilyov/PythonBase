# Version 1
def my_func(a, b):
    """
    Exponentiation function
    :param a: base
    :param b:power
    :return: pow
    """
    if float(a) > 0 and int(b) < 0:
        return round(a ** b, 7)
    else:
        print(f"Incorrect arguments a:{a}, b:{b}, conditions a > 0, b < 0")


print(my_func(6, -5))


# Version 2
def my_func_2(a, b):
    if float(a) > 0 and int(b) < 0:
        result = 1
        for i in range(abs(b)):
            result *= 1 / a
        return round(result, 7)
    else:
        print(f"Incorrect arguments a:{a}, b:{b}, conditions a > 0, b < 0")


print(my_func_2(b=-5, a=6))
