# IN = 'day1/testdata2.txt'  # exp 281
IN = 'day1/realdata.txt'


import re

# the ?= is a lookahead assertion, so it doesn't consume the character
NUMBERS = re.compile('(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
NUM2NUM = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

running_total = 0
for line in open(IN):
    print(line)
    line_list = [x for x in NUMBERS.findall(line)]
    print(line_list)
    converted_list = [NUM2NUM.get(x, x) for x in line_list]
    to_add = int(f'{converted_list[0]}{converted_list[-1]}')
    print(to_add)
    running_total += to_add

print(running_total)
