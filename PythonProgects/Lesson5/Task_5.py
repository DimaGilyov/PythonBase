from random import randint


def start_program():
    random_numbers = [str(randint(1, 100)) for _ in range(0, 9)]
    text = ' '.join(random_numbers)
    try:
        with open("text_5.txt", "w+", encoding="utf-8") as file_5:
            print(f"Write >>> {text}")
            file_5.write(text)

            file_5.seek(0)
            input_text = file_5.read()
            print(f"Read <<< {input_text}")

            numbers_list = map(lambda x: int(x), input_text.split(" "))
            print(f"Sum: {sum(numbers_list)}")

    except IOError as error:
        print(error)


start_program()
