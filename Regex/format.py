import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name): # := assign a value and ask a boolean question about it
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")