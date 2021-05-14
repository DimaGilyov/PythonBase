rating = [9, 7, 5, 5, 2]

while True:
    number = int(input("Enter natural number: "))
    if number > 0:
        for n, el in enumerate(rating):
            if number > el:
                rating.insert(n, number)
                break
            elif n == len(rating) - 1:
                rating.append(number)
                break

        break

print(rating)
