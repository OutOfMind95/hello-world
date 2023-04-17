def main():
    time = input("What is it? ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    if "a.m" or "p.m." in time:
        h_m, p = time.split(" ")
        h, m = h_m.split(":")
        if p == "p.m." and int(h) != 12:
            time = int(h) + 12
            return time
        elif p == "a.m.":
            time = int(h)
            return time
    else:
        h, m = h_m.split(":")
        time = float(h) + (float(m)/60)
        return time


if __name__ == "__main__":
    main()
