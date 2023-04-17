answer = str(input("What is the Answer of the Great Question of Life, the Universe and Everything? ")).strip()
answer = answer.lower()

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")