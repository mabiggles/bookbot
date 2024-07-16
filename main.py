def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = count_characters(text)
    list_of_characters = convert_dictionary(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    list_of_characters.sort(reverse=True, key=sort_on)
    for letter in list_of_characters:
        print(f"The '{letter['letter']}' character was found {letter['count']} times")
    print("--- End report ---")


def sort_on(dict):
    return dict['count']


def convert_dictionary(dict):
    converted = []
    for item in dict:
        d = {
            "letter" : item,
            "count" : dict[item]
        }
        converted.append(d)
    return converted


def count_characters(text):
    text = text.lower()
    dictionary = {}
    for letter in text:
        if letter.isalpha():
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
    return dictionary


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()