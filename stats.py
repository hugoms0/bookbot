import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    raise Exception(sys.exit(1))
else:
    book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


def count_book_words(file):
    num_words = len(get_book_text(book_path).split())
    return num_words

def count_book_chars(file):
    num_chars = {}
    book_text = get_book_text(book_path).lower()
    for char in book_text:
        if char not in num_chars:
            num_chars[char] = 1
        else:
            num_chars[char] += 1
    return num_chars

def sort_on(dict):
    return dict["num"]

def sort(dict):
    sorted_list = []
    unsorted_dict = count_book_chars(book_path)
    for char in unsorted_dict:
        if char.isalpha():
            char_dict = {}
            char_dict["char"] = char
            char_dict["num"] = unsorted_dict[char]
            sorted_list.append(char_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

