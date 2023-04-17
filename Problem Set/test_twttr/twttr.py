
def main():
    string = input("Input: ")
    string = shorten(string)
    string = string.strip()
    print("Output:", string)

def shorten(string):
    string = string.translate({ord(i): None for i in "aio.-1?"})

    return string


if __name__ == "__main__":
    main()
