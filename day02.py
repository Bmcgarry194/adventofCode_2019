'''
https://adventofcode.com/2019/day/2
'''

def parse(input):
    return [int(num) for num in input.strip().split(',')]

def intcode(raw_data, noun, verb, step=4):
    data = raw_data[:]
    data[1], data[2] = noun, verb
    i = 0
    while data[i] != 99:
        if data[i] == 1:
             data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        elif data[i] == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        else:
            print(f'{data[0]} is not a valid opcode')
            break
        i += step
    return data[0]

with open('data/day02_part1_input.txt') as f:
    raw_data = parse(f.read())

from itertools import product

for noun, verb in product(range(0, 100), range(0, 100)):
        if intcode(raw_data, noun, verb) == 19690720:
            print(noun, verb, intcode(raw_data, noun, verb))
            print(f'{100 * noun +verb}')
            break

