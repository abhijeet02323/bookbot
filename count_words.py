def get_file_path(filepath):
    with open(filepath, 'r') as book:
        content=book.read()
    return content 

def count_words(text):
    words=text.split()
    return len(words)

def main():
    book_text= get_file_path("./books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words in the book")

main()
   

