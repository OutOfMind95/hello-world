
def main():
    string = input("Input: ")
    string = shorten(string)
    print("Output:", string)

def shorten(string):
    vowel = [("a"),("e"),("i"),("o"),("u"),("A"),("E"),("I"),("O"),("U")]

    string = string.translate({ord(i): None for i in "aeiouAEIOU"})

    return string


if __name__ == "__main__":
    main()
