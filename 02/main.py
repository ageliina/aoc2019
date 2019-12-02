#!/usr/bin/env python3
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi

"""
aoc2019.2
"""

from itertools import product

opcodes = {1: lambda x, y: x + y,
           2: lambda x, y: x * y}

def decode(program, noun=None, verb=None):
    program = list(map(int, program.split(',')))
    pos = 0

    if noun and verb:
        program[1] = noun
        program[2] = verb

    while pos < len(program):
        opcode = program[pos]
        if opcode == 99 or opcode not in opcodes:
            pos += 1
            break
        else:
            pos1, pos2, pos3 = program[pos+1:pos+4]
            program[pos3] = opcodes[opcode](program[pos1], program[pos2])
        pos += 4
    return ','.join(str(p) for p in program)

assert decode("1,0,0,0,99") == "2,0,0,0,99"
assert decode("2,3,0,3,99") == "2,3,0,6,99"
assert decode("2,4,4,5,99,0") == "2,4,4,5,99,9801"
assert decode("1,1,1,4,99,5,6,0,99") == "30,1,1,4,2,5,6,0,99"

program = open("input", 'r').readline().strip()

for noun, verb in product(range(100), range(100)):
    output = decode(program, noun, verb)
    test = int(output.split(',')[0])
    if test == 3850704 or test == 19690720:
        print(test, 100 * noun + verb)
