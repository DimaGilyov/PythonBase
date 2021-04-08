def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    return sum(my_list[1:])


print(my_func(5, 3, 1))
