from collections import Counter

grocery_list = list()

while True:
    try:
        item = input().upper().strip()
        grocery_list.append(item)

    except EOFError:
        grocery_list = Counter(grocery_list)
        for item in sorted(grocery_list):
            print(grocery_list[item], end=" ")
            print(item)

        break
