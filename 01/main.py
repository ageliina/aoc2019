#!/usr/bin/env python3
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi

"""
aoc2019.1
"""

def fuel(mass, recursive=False):
    f = mass // 3 - 2
    if mass <= 0 or f <= 0:
        return 0
    return f + (fuel(f, True) if recursive else 0)

assert fuel(12), 2
assert fuel(14), 2
assert fuel(1969), 654
assert fuel(100756), 33583
assert fuel(14, True), 2
assert fuel(1969, True), 966
assert fuel(100756, True), 50346

mass = [int(l) for l in open("input", 'r')]
print(sum(fuel(m) for m in mass))
print(sum(fuel(m, True) for m in mass))
