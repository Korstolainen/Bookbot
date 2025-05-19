from stats import get_book_text
from stats import counting_words
from stats import counting_letters
from stats import sorting_dictionary_count

def main():
    link_to_book = "books/frankenstein.txt"
    book_contents = get_book_text(link_to_book)
    word_count = counting_words(book_contents)
    letter_count = counting_letters(book_contents)
    sorted_letter_count = sorting_dictionary_count(letter_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {link_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for letter_dict in sorted_letter_count:
        char = letter_dict["char"]  # Get the character from the dictionary
        if char.isalpha():  # Check if it's alphabetical
            num = letter_dict["num"]  # Get the count
            print(f"{char}: {num}")  # Print in required format

    print("============= END ===============")


    return

main()