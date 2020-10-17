import sys
import load_dictionary


def load(file: str):
    """
    テキストファイルを開いて、以下の処理をしつつリストに変換して返す

    - すべて小文字に変換
    - 1文字の単語が合った場合は除外
    """
    try:
        with open(file, "r") as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [
                x.lower() for x in loaded_txt if len(x) > 1
            ]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    print(load("./words.txt"))
