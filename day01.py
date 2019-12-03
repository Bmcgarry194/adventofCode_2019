'''
https://adventofcode.com/2019/day/1
'''

# Part 1
def calc_fuel(mass):
    return mass // 3 - 2

assert calc_fuel(100756) == 33583

with open('data/day01_input.txt') as f:
    data = f.read().strip().split('\n')

result = sum([calc_fuel(int(num)) for num in data])

# print(result)

# Part 2

def calc_fuel_rec(mass):
    new_mass = calc_fuel(mass)
    if new_mass <= 0:
        return 0
    else:
        return calc_fuel_rec(new_mass) + new_mass

#result2 = sum([calc_fuel_rec(int(num)) for num in data])

assert calc_fuel_rec(100756) == 50346

#print(result2)

