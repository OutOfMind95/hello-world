import sys

names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Ron"]

name = input("Name: ")

for name in names:
    print("Found")
    sys.exit(0)

print("Not Found")
sys.exit(1)