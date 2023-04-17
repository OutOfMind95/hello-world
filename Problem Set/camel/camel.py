string = input("camelCase: ").strip()

print("snake_case: ", end="")

for w in string:
    if w.isupper():
        w = "_" + w.lower()
        print(w, end="")
    else:
        print(w, end="")
print()
