def main():
    print_square(3)

def print_square(size):
    # for each row in sqaure
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print("#", end="")
        # move to new line
        print()

main()