import re
from Lab_9_Coin import images


states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
          "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
          "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
          "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
          "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
          "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
          "Wisconsin", "Wyoming"]
# Returns state names in the order in the document
# todo hacky way for now, edit if you find a better method
def get_states():
    states_reordered = []
    with open('quarter_info.txt', 'r', encoding='utf8') as f:
        for line in f:
            if line.title().strip() in states:
                states_reordered.append(line.title().strip())

    return states_reordered


# Returns the dates each coin was released into circulation
def get_dates():
    dates = []
    with open('quarter_info.txt', 'r', encoding='utf8') as f:
        for line in f:
            if 'Coin Release' in line:
                date = re.findall("Release: (.*) Release", line, re.DOTALL)
                dates.append(date[0])

    return dates


# Returns each coin's design description
# TODO many design descriptions are on multiple lines and don't have a universal stop character. How to deal with this?
def get_descriptions():
    years = ["1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007"]
    descriptions = []
    final = []
    description = ""
    with open('quarter_info.txt', 'r', encoding='utf8') as f:
        try:
            for line in f:
                if 'Design: ' in line:
                    description = (re.findall("Design: (.*) .", line, re.DOTALL)) + (re.findall("\s(\w+)$", line, re.DOTALL))
                    nextline = next(f).strip()
                    while (nextline.title() not in states) and (nextline not in years):
                        description.append(nextline)
                        nextline = next(f).strip()
                    descriptions.append(description)
        except:
            descriptions.append(description)

    for x in descriptions:
        concat = ' '.join(x)
        final.append(concat)

    return final

desc = get_descriptions()
for x in desc:
    print(x)