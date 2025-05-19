def get_book_text(path_to_book):#------------Takes a filepath as input. Returns a string with the text from the file
    book = None
    with open(path_to_book) as text:
        book = text.read()
    return book

def counting_words(text):#-------------------Takes a string as input. Counts the separate words. prints the count of words
    count = 0
    words = text.split()    #splitting text in to a list of words
    for word in words:
        count = count + 1          #counting each word
    return count

    


def main():
    book_contents = get_book_text("books/frankenstein.txt")
    word_count = counting_words(book_contents)
    print(f"{word_count} words found in the document")
    return

main()