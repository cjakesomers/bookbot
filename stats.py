def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()

def count_words(book):
    chars = book.split()
    return len(chars)

def char_counts(book):
    book = book.lower()
    char_counts = {}
    for char in book:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts
    
def get_sorted(book):
    def sort_on(tup):
        return tup[1]
    char_counter = char_counts(book)
    char_list = []
    temp_tup = ()
    while len(char_counter) != 0:
        temp_tup = char_counter.popitem()
        if temp_tup[0].isalpha():
            char_list.append(temp_tup)
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    