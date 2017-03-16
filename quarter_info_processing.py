import re

quarter_data = []
design_data = []

# This section works, and will return the dates the coin was released into circulation.
with open('quarter_info.txt', 'r') as info:

    for line in info:

        if 'Coin Release' in line:

            testRE = re.findall("Release: (.*) Release", line, re.DOTALL)
            quarter_data.append(testRE)

# This code will eventually add the Design description . TODO this is not working.
with open('quarter_info.txt', 'r') as info:

    for line in info:

        if 'Design' in line:

            testRE = re.findall("Design: (.*) ", line, re.DOTALL)

            design_data.append(testRE)

print(design_data)
