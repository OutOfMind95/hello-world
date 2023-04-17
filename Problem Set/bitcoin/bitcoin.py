import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        n = sys.argv[1]
        n = float(n)
    except ValueError:
        sys.exit("Command-line argument is not a number")
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    j = r.json()
except requests.RequestExeption:
    sys.exit("Load Fail.")

rate = j["bpi"]["USD"]["rate_float"]
rate = float(rate)

cost = n * rate

print(f"${cost:,.4f}")


