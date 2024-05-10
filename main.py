def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    chars = get_chars_dict(text)
    print_report(book_path, words, chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()


# count words in text file
def count_words(text):
    return len(text.split())


# count each letters appearances in text file
def get_chars_dict(text):
    letters = {}
    for letter in text:
        letter = letter.lower()
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    # sort dict based on occurances
    letters = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
    return letters


def print_report(path, words, chars):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document", end="\n\n")

    for letter, count in chars.items():
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")
    print(f"--- End report ---")


main()
