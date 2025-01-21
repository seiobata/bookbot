def main():
    print(file_contents)
    word_count()

def word_count():
    words = file_contents.split()
    count = 0
    for word in words:
        count += 1
    print(f"{count} number of words in document")
    
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

main()
