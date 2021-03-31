number = int(input("Enter number: "))

max_number = 0
while True:
    last_number = number % 10
    if last_number == 0:
        break

    if last_number > max_number:
        max_number = last_number

    number = number // 10

print(f"Max number is {max_number}")
