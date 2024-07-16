def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print(count_characters(text))

def count_characters(text):
    text = text.lower()

    dictionary = {}
    for letter in text:
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