'''Day 4: Secure Container'''

'''It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).'''

'''How many different passwords within the range given in your puzzle input meet these criteria?'''

INPUT = '''183564-657474'''

from collections import Counter

def parse(input):
    start, stop = input.split('-')
    return range(int(start), int(stop))

def val_pass(password):
    has_double = False
    is_ascending = True
    for current, next in zip(password, password[1:]):
        current, next = int(current), int(next)
        if current > next:
            is_ascending = False
        if current == next:
            has_double = True

    return has_double and is_ascending

count_passes = 0
for i, x in enumerate(parse(INPUT)):
    if val_pass(str(x)):
        count_passes += 1
print(count_passes)
# TEST CASES

assert val_pass('111111') == True
assert val_pass('223450') == False
assert val_pass('123789') == False

# Part 2

def val_pass_only_doubles(password):
    has_double = False
    is_ascending = True
    counts = Counter(str(password)) 
    for current, next in zip(password, password[1:]):
        current, next = int(current), int(next)
        if current > next:
            is_ascending = False
        if current == next and counts[str(current)] == 2:
            has_double = True
    return has_double and is_ascending

count_passes = 0
for i, x in enumerate(parse(INPUT)):
    if val_pass_only_doubles(str(x)):
        count_passes += 1
print(count_passes)

