import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^((?:\d)(?:\d)?(?:\d)?)\.((?:\d)(?:\d)?(?:\d)?)\.((?:\d)(?:\d)?(?:\d)?)\.((?:\d)(?:\d)?(?:\d)?)$", ip, re.ASCII):
        num1 = int(matches.group(1))
        num2 = int(matches.group(2))
        num3 = int(matches.group(3))
        num4 = int(matches.group(4))
    else:
        return False

    if 0 <= num1 <= 255:
        if 0 <= num2 <= 255:
            if 0 <= num3 <= 255:
                if 0 <= num4 <= 255:
                    return True
                else:
                    return False

            else:
                return False
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
