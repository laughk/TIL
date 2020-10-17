import typing as t

import sys
import load_dictionary


SINGLE_WORD = ("a", "i")


def cleanup(words: t.List[str]) -> t.List[str]:
    """
    words の中に一文字のものは原則除外する。
    ただし、1文字で意味をなす単語(SINGLE_WORD)はそのまま保持する
    """
    cleaned_words = []

    for word in words:
        if len(word) > 1:
            cleaned_words.append(word)
        elif len(word) == 1 and word in SINGLE_WORD:
            cleaned_words.append(word)

    return cleaned_words


if __name__ == "__main__":

    words = load_dictionary.load("./words.txt")
    print(cleanup(words))
