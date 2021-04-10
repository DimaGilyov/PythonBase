from functools import reduce


def range_sum(previous_element, current_element):
    return previous_element * current_element


# В принципе мы могли просто воспользоваться range(100, 1001, 2), но раз в задании просят использовать возможности
# генератора, то используем это
my_range = [el for el in range(100, 1001) if el % 2 == 0]

result = reduce(range_sum, my_range)
# OMG, какое большое число =)
print(result)
