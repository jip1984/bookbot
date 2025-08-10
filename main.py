import sys
from stats import count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def number_of_words(text):
    return len(text.split())

def print_report(path: str, word_total: int, sorted_chars: list[dict]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_total} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    # require exactly one argument: the path to the book
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_total = number_of_words(text)
    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)
    print_report(book_path, word_total, sorted_chars)

if __name__ == "__main__":
    main()
