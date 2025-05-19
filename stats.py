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

def counting_letters(text):#-----------------Takes a string as input. Turns all letters to lowercase. Counts each use of a letter. Returns a dictionary of each letter as key and how many times the letter has been used.
    count = {}
    text_lowercase = text.lower()
    for char in text_lowercase:
        count[char] = count.get(char, 0) + 1 #Will check if the character is on the list, if it is, it will add 1 to its count, if not it will create the dictionary key for the character, set its count to 0 and add 1
    return count


def sorting_dictionary_count(dict):#----------Takes a dictionary, turns that in to a list of dictionaries where {"char": "b", "num": 4868}
    dict_list = []
    for key in dict:
        dict_list.append({"char": key, "num" : dict[key]})#Iterate trought the dictionary and create a list of dictionaries
    
    dict_list.sort(key=lambda d: d["num"], reverse=True)#Sort the list of dictionaries. (lambda d: d["num"] is jut a quick way to create a fucntion since the key parameter imputs a function)

    return dict_list
