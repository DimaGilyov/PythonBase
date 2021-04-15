def print_words_count_in_lines(lines):
    words_count_dict = {n + 1: len(line.split()) for n, line in enumerate(lines)}
    for key, value in words_count_dict.items():
        print(f"{key}) words count: {value}")


try:
    with open("text_2.txt", "r", encoding="utf-8") as file_2:
        text = [line.strip() for line in file_2.readlines()]
        print(f"Lines count: {len(text)}")
        print_words_count_in_lines(text)
except IOError as error:
    print(error)
