def main():
    book = "books/frankenstein.txt"
    text = book_text(book)
    words_counted = word_count(text)
    chars_counted = chars_count(text)
    list_sorted = dict_to_sorted_list(chars_counted)

    print(f"There are {words_counted} number of words in {book}")
    for i in list_sorted:
        if i["char"].isalpha():
            print(f"The '{i["char"]}' character was found {i["num"]} times")

def book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    count = text.split()
    return len(count)

def chars_count(text):
    dict_of_chars = {}
    text = text.lower()
    for i in text:
        if i in dict_of_chars:
            dict_of_chars[i] += 1
        else:
            dict_of_chars[i] = 1
    return dict_of_chars

def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(unsorted_dict):
    sorted_list = []
    for i in unsorted_dict:
        sorted_list.append({"char": i, "num": unsorted_dict[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
