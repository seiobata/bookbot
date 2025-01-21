def main():
    print(file_contents)
    word_count()
    character_count()

def word_count():
    words = file_contents.split()
    count = len(words)
    print(f"{count} number of words in document")

def character_count():
    dict_of_chars = {}
    lower_file_contents = file_contents.lower()
    for i in lower_file_contents:
        if i in dict_of_chars:
            dict_of_chars[i] += 1
        else:
            dict_of_chars[i] = 1
    print(dict_of_chars)
    
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

main()
