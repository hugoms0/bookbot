
def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


def count_book_words(file):
    num_words = len(get_book_text("books/frankenstein.txt").split())
    print(f"{num_words} words found in the document")
    return num_words