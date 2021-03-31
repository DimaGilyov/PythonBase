# n + nn + nnn
input_number = int(input("Enter number: "))

i = 0
_sum = 0
number = input_number
while i < 3:
    _sum += number
    number = int(str(number) + str(input_number))
    i += 1

print(f"Number:{input_number}, sum:{_sum}")

