#!/usr/bin/env python3
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi

"""
aoc2019.4
"""

low, high = 284639, 748759

count = 0
for i in range(low, high + 1):
    number = str(i)
    if sorted(number) != list(number):
        continue
    g = {j: number.count(str(j)) for j in range(10)}
    if 2 not in g.values():
        continue
    count += 1
print(count)
