import string

s = input("Enter a string: ")

letter = 0
space = 0
digit = 0
other = 0

for c in s:
    if c.isalpha():
        letter += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        other += 1

print('There are\n%d letters,\n%d spaces,\n%d digits,\n%d other.' % (letter, space, digit, other))