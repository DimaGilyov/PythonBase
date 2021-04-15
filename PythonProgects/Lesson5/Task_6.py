def start_program():
    try:
        text = [line.strip() for line in open("text_6.txt", "r", encoding="utf-8")]
        parse_text_to_key_value_pairs(text)
    except IOError as error:
        print(error)


def parse_text_to_key_value_pairs(text):
    academic_subjects = {}
    for line in text:
        split_text = line.split(":")
        key = split_text[0]
        value = split_text[1]
        academic_subjects[key] = get_hours_count(value)
    print(academic_subjects)


def get_hours_count(text):
    hours_str = str(text).replace("-", "").replace("(пр)", "").replace("(л)", "").replace("(лаб)", "").split()
    hours = map(lambda x: int(x), hours_str)
    return sum(hours)


start_program()
