import sys
from src.utils import load_text


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Args should be more the one")
        exit(1)
    print(load_text(argv[1]))
