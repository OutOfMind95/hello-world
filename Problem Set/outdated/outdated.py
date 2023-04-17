import re

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    date = input("Date: ").strip()
    if matches := re.search(r"([0-9]+)/([0-9]+)/([0-9]+)", date):
        m = int(matches.group(1))
        d = int(matches.group(2))
        y = int(matches.group(3))
        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f"{y}-{m:02}-{d:02}")
            break
    elif matches := re.search(r"([a-zA-z]+) ([0-9]+), ([0-9]+)", date):
        m = matches.group(1)
        m = month.index(m) + 1
        d = int(matches.group(2))
        y = int(matches.group(3))
        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f"{y}-{m:02}-{d:02}")
            break
