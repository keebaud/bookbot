def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report(book_path, text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_letters(book_text):
    char_dictionary = {}
    for char in book_text:
        lower_c = char.lower()
        if lower_c in char_dictionary:
            char_dictionary[lower_c] += 1
        else:
            char_dictionary[lower_c] = 1
    return char_dictionary

def list_from_dict(in_dict):
    output = []
    for item in in_dict:
        if item.isalpha():
            i_set = {}
            i_set["character"] = item
            i_set["count"] = in_dict[item]
            output.append(i_set)
    return output

def sort_on(dict):
    return dict["count"]

def report(path, book_text):
    print(f"-- Begin report of {path} ---")
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")
    print()
    letters = list_from_dict(count_letters(book_text))
    letters.sort(reverse=True, key=sort_on)
    for letter in letters:
        char = letter["character"]
        count = letter["count"]
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
    
main()
