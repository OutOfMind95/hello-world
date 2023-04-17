import random

while True:
    try:
        level = int(input("Level: "))
        if level < 0:
            level = int(input("Level: "))
        solution = random.randint(1, level)
        while True:
            guess = int(input("Guess: "))
            if guess < 0:
                guess = int(input("Guess: "))
            if guess < solution:
                print("Too small!")
            elif guess > solution:
                print("Too Large!")
            else:
                print("Just right!")
                break
        break

    except ValueError:
        print()