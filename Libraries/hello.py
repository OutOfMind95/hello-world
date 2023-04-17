from sys import argv, exit

# Check for error
if len(argv) < 2:
    exit("Please give arguments")

# Print name tags
for arg in argv[1:]:
    print("Hello, my name is", arg)