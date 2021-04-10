def fact(number):
    result = 1
    for n in range(1, number + 1):
        result *= n
        yield result


for i, el in enumerate(fact(5), 1):
    print(f"{i}! = {el}")
