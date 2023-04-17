import re

url = input("URL: ").strip()

if matches := re.search(r"^(?:https?://)?.*twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    username = matches.group(1)
    print(f"Username: @{username}")