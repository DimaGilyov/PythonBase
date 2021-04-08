def start():
    result = 0
    while True:
        text = input("Enter numbers separated by space (Exit: Q): 1 2 3 ....Q: ")
        values_list = text.split()
        _sum = 0
        for element in values_list:
            if element.upper() == "Q":
                result += _sum
                print(f"Result: {result}")
                return
            elif element.isdigit():
                _sum += float(element)
                print(f"Result={result}, sum={_sum}")
        result += _sum


start()
