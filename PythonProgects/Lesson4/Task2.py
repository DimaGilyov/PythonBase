numbers_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"{numbers_list}")

filtered_list = [numbers_list[i] for i in range(1, len(numbers_list)) if numbers_list[i] > numbers_list[i - 1]]
print(f"{filtered_list}")
