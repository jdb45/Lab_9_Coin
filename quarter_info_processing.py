import re


# Returns the dates each coin was released into circulation
def get_dates():
    dates = []
    with open('quarter_info.txt', 'r', encoding='utf8') as info:
        for line in info:
            if 'Coin Release' in line:
                date = re.findall("Release: (.*) Release", line, re.DOTALL)
                dates.append(date[0])

    return dates


# Returns each coin's design description
# TODO many design descriptions are on multiple lines and don't have a universal stop character. How to deal with this?
def get_descriptions():
    descriptions = []
    with open('quarter_info.txt', 'r', encoding='utf8') as info:
        for line in info:
            if 'Delaware' in line:
                description = re.findall("Design: (.*) C", line, re.DOTALL)
                descriptions.append(description)

dates = get_dates()
print(dates)
print(get_descriptions())