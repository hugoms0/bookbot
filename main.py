from stats import count_book_words, sort
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        raise Exception(sys.exit(1))
    else:
        book_path = sys.argv[1]

        sorted_book_char_count_list = sort(book_path)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {count_book_words(book_path)} total words")
        print("--------- Character Count -------")
        for i in range(len(sorted_book_char_count_list)):
            print(f"{sorted_book_char_count_list[i]["char"]}: {sorted_book_char_count_list[i]["num"]}")
        print("============= END ===============")
    return 
main()