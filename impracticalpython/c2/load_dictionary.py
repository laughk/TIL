import sys

def load(file: str):
    """テキストファイルを開いて、内容を小文字の文字列のリストに変換する"""
    try:
        with open(file, "r") as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    print(load("./words.txt"))
