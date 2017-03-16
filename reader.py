import re


def get_dates():
    dates = []

    with open("quarter-info.txt", encoding="utf8") as f:
        for line in f:
            if "Coin Release: " in line:
                date = re.findall("Release: (.*) Release", line, re.DOTALL)
                dates.append(date)
