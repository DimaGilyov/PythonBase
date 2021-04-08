# Задача 6 и 7
def int_func(*args):
    """
    Convert text to title
    :param args: text
    :return: title
    """
    words_list = []
    for el in args:
        el = str(el)
        words_list.append(el.title())
    return words_list


def int_func_2(words):
    words = words.split(",")
    return int_func(*words)


print(*int_func("hello", "world"))
print(*int_func_2("hello, world, dima"))

