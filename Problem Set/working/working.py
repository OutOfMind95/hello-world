import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(1[0-2]|[1-9]):([0-5][0-9]) (AM|PM) to (1[0-2]|[1-9]):([0-5][0-9]) (AM|PM)$", s):
        h1 = int(matches.group(1))
        m1 = matches.group(2)
        am_pm1 = matches.group(3)
        h2 = int(matches.group(4))
        m2 = matches.group(5)
        am_pm2 = matches.group(6)

        if am_pm1 == "PM":
            h1 += 12
            if h1 == 24:
                h1 = 12
        elif am_pm2 == "PM":
            h2 += 12
            if h2 == 24:
                h2 = 12

        if am_pm1 == "AM":
            if h1 == 12:
                h1 = 0
        elif am_pm2 == "AM":
            if h2 == 12:
                h2 = 0
                
        return f"{h1:02d}:{m1} to {h2:02d}:{m2}"
    elif matches := re.search(r"^(1[0-2]|[1-9]) (AM|PM) to (1[0-2]|[1-9]) (AM|PM)$", s):
        h1 = int(matches.group(1))
        am_pm1 = matches.group(2)
        h2 = int(matches.group(3))
        am_pm2 = matches.group(4)

        if am_pm1 == "PM":
            h1 += 12
            if h1 == 24:
                h1 = 12
        elif am_pm2 == "PM":
            h2 += 12
            if h2 == 24:
                h2 = 12

        if am_pm1 == "AM":
            if h1 == 12:
                h1 = 0
        elif am_pm2 == "AM":
            if h2 == 12:
                h2 = 0

        return f"{h1:02d}:00 to {h2:02d}:00"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
