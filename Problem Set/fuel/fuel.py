while True:
    fuel = input("Fraction: ")
    try:
        x, y = fuel.split("/")
        x = int(x)
        y = int(y)
        percentage = x / y
        if percentage <= 1:
            break
    except(ValueError, ZeroDivisionError):
        print(end="")

percentage = percentage * 100
p = int(round(percentage))
if 0 <= p <= 1:
    print("E")
elif 99 <= p <= 100:
    print("F")
else:
    print(f"{p}%")
