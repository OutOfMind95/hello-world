def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True: # infite loop
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
main()