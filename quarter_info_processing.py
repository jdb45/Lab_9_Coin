import re

quarter_data = []

with open('quarter_info.txt', 'r') as info:

    for line in info:

        if 'Coin Release' in line:

            print(line)
