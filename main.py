def get_book_text(path_to_book):
    book = None
    with open(path_to_book) as text:
        book = text.read()
    return book


def main():
    print(get_book_text("books/frankenstein.txt"))
    return

main()