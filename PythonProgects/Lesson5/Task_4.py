# Версия 1
def translate_to_rus_v1(english_text):
    english_text = str(english_text)
    if "One" in english_text:
        return english_text.replace("One", "Один")
    elif "Two" in english_text:
        return english_text.replace("Two", "Два")
    elif "Three" in english_text:
        return english_text.replace("Three", "Три")
    else:
        return english_text.replace("Four", "Четыре")


def print_new_file_v1(eng_text):
    try:
        with open("new_text_4.txt", "w", encoding="utf-8") as new_file_4:
            [new_file_4.write(translate_to_rus_v1(line)) for line in eng_text]
    except IOError as io_error:
        print(io_error)
# ---------------------------------------------------------------------------------


# Версия 2
def translate_to_rus_v2(english_text_lines):
    eng_rus_words = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    rus_text = []
    for eng_text in english_text_lines:
        eng_word = eng_text.split("-")[0].strip()
        rus_text.append(eng_text.replace(eng_word, eng_rus_words[eng_word]))
    return rus_text


def print_new_file_v2(eng_text):
    try:
        with open("new_text_4.txt", "w", encoding="utf-8") as new_file_4:
            [new_file_4.write(line) for line in translate_to_rus_v2(eng_text)]
    except IOError as io_error:
        print(io_error)


try:
    with open("text_4.txt", "r", encoding="utf-8") as file_4:
        all_text = file_4.readlines()
        # print_new_file_v1(all_text)
        print_new_file_v2(all_text)
except IOError as error:
    print(error)
