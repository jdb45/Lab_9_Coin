import re

with open("page.txt", encoding="utf8") as f:
    for line in f:
        if "Coin Release: " in line:
            print(line)

test_string = "Statehood: December 7, 1787 Coin Release: January 4, 1999 Release Order: 1 Total Mintage for Circulation: 774,824,000"
testRE = re.findall("Release: (.*)Release", test_string, re.DOTALL)
print(testRE)