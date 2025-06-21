from stats import word_counts


def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    text = get_book_text('books/frankenstein.txt')
    #word_total(text)
    #print(text[:500]V)
    d = word_counts(text)
    print(d)


main()
