def get_book_text(filepath):
    with open(filepath, 'r') as book:
        return  book.read()

def main():
    book_content = get_book_text("books/frankenstein.txt")
    
    print(book_content)

main()
