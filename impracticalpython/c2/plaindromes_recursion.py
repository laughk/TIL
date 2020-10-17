import typing as t
import load_dictionary

word_list = load_dictionary.load("words.txt")
pali_list = []


def check_palindrome(word: str) -> bool:

    word_len = len(word)

    if word_len == 1:
        return True

    if word[0] == word[-1]:
        if word_len == 2:
            return True
        else:
            return check_palindrome(
                word.lstrip(word[0]).rstrip(word[-1])
            )

    return False


if __name__ == "__main__":

    pali_list = [word for word in word_list if check_palindrome(word)]

    print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
    print(*pali_list, sep="\n")
