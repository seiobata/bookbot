def main():
    print(file_contents)
    
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

main()
