inp = str(input("File name: ")).strip().lower()

suffix = []

while True:
    if inp.endswith(("jpg", "jpeg", "png", "gif", "zip", "pdf", "txt")):
        suffix = inp.split(".")
        if len(suffix) > 2:
            suffix[1] = suffix[2]
        if suffix[1] in ("gif", "png", "jpg", "jpeg"):
            if suffix[1] == "jpg":
                suffix[1] = "jpeg"
            print(f"image/{suffix[1]}")
            break
        elif suffix[1] == "txt":
            print(f"text/{suffix[0]}")
            break
        elif suffix[1] in ("zip", "pdf"):
            print(f"application/{suffix[1]}")
            break
        else:
            print("application/octet-stream")
            break
    else:
        print("application/octet-stream")
        break