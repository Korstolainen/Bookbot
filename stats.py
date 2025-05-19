def get_book_text(path_to_book):#------------Takes a filepath as input. Returns a string with the text from the file
    book = None
    with open(path_to_book) as text:
        book = text.read()
    return book

def counting_words(text):#-------------------Takes a string as input. Counts the separate words. Returns the count of words as an INT
    count = 0
    words = text.split()    #splitting text in to a list of words
    for word in words:
        count = count + 1          #counting each word
    return count

def counting_letters(text):#-----------------Takes a string as input. Turns all letters to lowercase. Counts each use of a letter. Returns a dictionary of each letter and how many times it has been used.
    count = {}
    text_lowercase = text.lower()
    for char in text_lowercase:
        count[char] = count.get(char, 0) + 1 #count.get(char, 0) +1 will check if the character is on the list, if it is it will add 1 to its count, if not it will create the dictionary key for the character, set its count to 0 and add 1
    return count