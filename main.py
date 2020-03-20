# main.py- a simple program that determines whether a one-to-one character mapping exists from one string,
# word1, to another string, word2.
# For example, given s1 = abc and s2 = bcd, print "true" into stdout since we can map each
# character in "abc" to a character in "bcd".
# Given s1 = foo and s2 = bar, print "false" since the character ‘o’ cannot map to two characters.
# But given s1 = bar and s2 = foo, print "true" since each character in "bar" can be mapped to a
# character in "foo"
#
# Requires two string inputs of the same length, the first will try to be mapped onto the second.
# Author: Justin Kolodny


import sys


def main():
    # These are where the words are stored
    word_one = sys.argv[1]
    word_two = sys.argv[2]
    # We make both words lowercase for convenience sake
    word_one = word_one.lower()
    word_two = word_two.lower()
    # A simple array of the alphabet
    # Represents what each letter currently maps to, so the letter at the 0th is what the letter 'a' maps to,
    # 2nd index will show us what 'c' maps to and so on.
    # By default every letter simply maps to itself.
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "w", "x", "y", "z"]
    # Goes through all of the characters in the word.
    for character in range(0, len(word_one)):
        # Turns the letter into its number mod 26 using ascii math, this will help us access what that letter is mapped
        # to in the alphabet_array.
        which_letter = ord(word_one[character]) - 97
        # If the letter in the first word already maps to the correct letter in the second word we simply move on.
        if alphabet_array[which_letter] == word_two[character]:
            continue
        else:
            # If the letter doesn't already currently point to it's default letter and it needs to change again
            # in order to correctly map to word2, the program prints false and exits.
            if alphabet_array[which_letter] != chr(which_letter+97):
                print("false")
                sys.exit(0)
            # Otherwise the letter gets mapped to the letter in the second word.
            else:
                alphabet_array[which_letter] = word_two[character]
    # If we make it through this process without failing, we print out true.
    print("true")


if __name__ == "__main__":
    main()
