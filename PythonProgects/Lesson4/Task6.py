from itertools import count
from itertools import cycle

# Задание 1
for el in count(9):
    if el > 20:
        break
    else:
        print(el)


# Задание 2
words_list = ["Hello", "my", "dear", "friend"]
count = 0
for el in cycle(words_list):
    if count >= 3 * len(words_list):
        break
    else:
        print(el)
        count += 1

