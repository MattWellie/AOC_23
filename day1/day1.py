# IN = 'day1/testdata.txt'
IN = 'day1/realdata.txt'  # 54916

import re

NUMBERS = re.compile(r'(\d)')

running_total = 0
for line in open(IN):
    line_list = [x for x in NUMBERS.findall(line)]
    to_add = int(f'{line_list[0]}{line_list[-1]}')
    print(line_list)
    print(to_add)
    running_total += to_add

print(running_total)