from stats import get_book_text
from stats import counting_words
from stats import counting_letters

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    word_count = counting_words(book_contents)
    letter_count = counting_letters(book_contents)
    print(f"{word_count} words found in the document")
    print(letter_count)
    return

main()