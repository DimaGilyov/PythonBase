input_text = input("Enter numbers separated by commas. '1, 2, 3 ...': ")
numbers_list = input_text.replace(" ", "").split(",")

i = 0
while i < len(numbers_list):
    if not numbers_list[i].isdigit():
        print("Unsupported text")
        input_text = input("Enter numbers separated by commas. '1, 2, 3 ...': ")
        numbers_list = input_text.replace(" ", "").split(",")
        i = 0
    else:
        i += 1

j = 0
while j < len(numbers_list) - 1:
    first_element, second_element = numbers_list[j], numbers_list[j + 1]
    numbers_list[j], numbers_list[j + 1] = second_element, first_element
    j += 2

print(numbers_list)
