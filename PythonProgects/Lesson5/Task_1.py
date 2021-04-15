try:
    with open("text_1.txt", "w+", encoding="utf-8") as file_1:
        while True:
            input_text = input("Enter text (exit - Enter): ")
            if input_text == "":
                break

            print(input_text, file=file_1, end="\n")
except IOError as error:
    print(error)
