my_list = [1, 2.3, True, "string", [1, 2, 3], (1, 2, 3), {1, 2, 3}, frozenset((1, 2, 3)), {1: "Str1", 2: "Str2"}]

for el in my_list:
    print(f"{type(el)}: {el}")
