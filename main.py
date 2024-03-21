def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_count = count_text(text)
    num_of_char = get_char_num(text)
    print(text)
    print(text_count)
    print(num_of_char)

def get_char_num(book_words):
    duped_chars = {}
    for char in book_words:
        lower = char.lower()
        if lower in duped_chars:
            duped_chars[lower] += 1
        else:
            duped_chars[lower] = 1
    return duped_chars


def count_text(book):
    words_in_book = book.split()
    return len(words_in_book)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()