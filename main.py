def main():
    filename = "books/frankenstein.txt"
    with open(filename, "r", encoding="UTF-8") as file:
        file_contents = file.read()
        word_count = get_word_count(file_contents)
        char_count = get_char_count(file_contents)
        print_report(filename, word_count, char_count)


def get_word_count(string):
    words = string.split()
    return len(words)


def get_char_count(string):
    char_count = {}
    for char in string:
        if char.isalpha():
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return sorted(char_count.items(), key=lambda i: i[1], reverse=True)


def print_report(filename, wc, chars):
    print(f"--- Begin report of {filename} ---")
    print(f"{wc} words found in the document\n")

    for ch in chars:
        print(f"The '{ch[0]}' character was found {ch[1]} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()
