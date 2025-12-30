from stats import *
import sys
def main():
    if(len(sys.argv) <= 1):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    num_words = count_words(book)
    sorted_chars = get_sorted(book)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for tup in sorted_chars:
        print(f"{tup[0]}: {tup[1]}")
    print("============= END ===============")
main()