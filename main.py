import sys


def main():
    word_one = sys.argv[1]
    word_two = sys.argv[2]
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "w", "x", "y", "z"]
    # print(word_one, word_two)
    for character in range(0, len(word_one)):
        which_letter = ord(word_one[character]) - 97
        if alphabet_array[which_letter] == word_two[character]:
            continue
        else:
            if alphabet_array[which_letter] != chr(which_letter+97):
                print("false")
                sys.exit(0)
            else:
                alphabet_array[which_letter] = word_two[character]
    print("true")


if __name__ == "__main__":
    main()
