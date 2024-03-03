def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    sorted_letters_list = sort_chars_to_list(count_letters(text))
    
    print(f"----- Report on {book_path} -----")
    print(f"Words found in document: {number_of_words}\n")

    for letter in sorted_letters_list:
        print(f"The letter {letter['char']} was found {letter['num']} times")
    
    print("----- End of Report -----")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(words):
    wordcount = words.split()
    return len(wordcount)

def count_letters(words):
    chars = {}
    for c in words:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]


def sort_chars_to_list(letter_dict):
    sorted_list = []
    for letter in letter_dict:
        sorted_list.append({"char": letter, "num": letter_dict[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()