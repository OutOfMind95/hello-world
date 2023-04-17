# simple input - output | Ask user to input their name
# name = input(str("What's you name? "))

# Remove whitespace from string
# name = name.strip()

# Capitalize user's name
# name = name.capitalize()

# Capitalize every first word
# name = name.title()

# Remove whitespace and Capitalize every first word

# name = name.strip().title()

# print("hello,", name)
# print(f"hello, {name}") #f -> formatta


# ** Tutto ciò è possibile con due singole linee di codice **

name = input(str("What's you name? ")).strip().title()
print(f"hello, {name}")