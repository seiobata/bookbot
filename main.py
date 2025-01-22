def main():
    text = book_text("books/frankenstein.txt")
    word_count(text)
    dict_report = character_count(text)
    character_report(dict_report)

def word_count(text):
    words = text.split()
    count = len(words)
    print(f"{len(words)} number of words in document")

def character_count(text):
    dict_of_chars = {}
    lowered_text = text.lower()
    for i in lowered_text:
        if i in dict_of_chars:
            dict_of_chars[i] += 1
        else:
            dict_of_chars[i] = 1
    return dict_of_chars

def character_report(text):
    start_chars = text
    for letter, value in start_chars.items():
        if letter.isalpha():
            print(f"The '{letter}' character was found {value} times")

def book_text(path):
    with open(path) as f:
        return f.read()

main()
