def divide_numbers(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print(f"Error when a number is divided by zero (0).")


num_1 = float(input("Enter number №1: "))
num_2 = float(input("Enter number №2: "))
print(divide_numbers(num_1, num_2))
