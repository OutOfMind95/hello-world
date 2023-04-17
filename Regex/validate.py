import re

email = input("What's your email? ").strip()

if re.search(r"^[a-z0-9_\.]+@(\w+\.)?\w+\.(edu|com|org|gov)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

                                        # re.search(pattern, string, flags=0) | r = row string | ^ inizio stringa $ fine stringa | \w any alphanumeric word

                                        # patter : A|B A or B
                                        #          (...) a group
                                        #          (?:...) non capturing version
                                        # re.IGNORECASE - lower or upper case is ignored
                                        # re.MULTILINE - march multiple line
                                        # re.DOTALL

                                        # . any character exc new line
                                        # * 0 or more repetition
                                        # 1 or more repetition
                                        # ? 0 or 1 repetition
                                        # {m} m repetition
                                        # {m,n} from m to n repetition