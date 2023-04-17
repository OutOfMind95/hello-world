import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    while True:
        counter = re.findall(r"\bum\b", s, re.IGNORECASE)
        counter = len(counter)
        if counter is None:
            return 0
        else:
            return counter


if __name__ == "__main__":
    main()
