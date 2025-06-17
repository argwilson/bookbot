import sys
from stats import get_num_words, get_num_characters, sorted_dict_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    frankenstein = get_book_text(filepath)
    frankenstein_count = get_num_words(frankenstein)
    frankenstein_dict = get_num_characters(frankenstein)
    frankenstein_list = sorted_dict_list(frankenstein_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {frankenstein_count} total words")
    print("--------- Character Count -------")
    for element in frankenstein_list:
        if element['char'].isalpha()==True:
            print(f"{element['char']}: {element['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()