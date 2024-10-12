def main():
    with open("books/frankenstein.txt", "r", encoding="UTF-8") as file:
        file_contents = file.read()
        print(file_contents)


if __name__ == "__main__":
    main()
