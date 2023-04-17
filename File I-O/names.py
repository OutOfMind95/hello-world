name = input("What's your name? ")

with open("names.csv", "a") as file: # apri e chiudi salvando
    file.write(f"{name}\n")
