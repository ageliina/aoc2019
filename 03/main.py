#!/usr/bin/env python3
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi

"""
aoc2019.3
"""

import sys
import numpy as np
from numpy import array

def test(observed, expected):
    try:
        assert (observed == expected).all(), "Error\n\tobserved: %s\n\texpected: %s" \
                                             % (str(observed), str(expected))
    except AttributeError:
        assert observed == expected, "Error\n\tobserved: %s\n\texpected: %s" \
                                      % (str(observed), str(expected))

def main1():

    def f(wires):

        wires = [w.split(',') for w in wires.split('\n')]

        paths = []
        pathsi = []
        for wire in wires:
            x, y = 0, 0
            path = []
            pathi = []
            for value in wire:
                v = int(value[1:])
                for _v in range(1, v + 1):
                    if "U" in value: y += 1
                    if "R" in value: x += 1
                    if "D" in value: y -= 1
                    if "L" in value: x -= 1
                    path.append((x, y))
                    pathi.append(10**6 * x + y)
            paths.append(path)
            pathsi.append(pathi)

        crosses = np.in1d(pathsi[0], pathsi[1])
        crosses = np.array(paths[0])[crosses]

        distances = []
        path0 = (0, 0)
        for cross in crosses:
            d = abs(cross[0] - path0[0]) + abs(cross[1] - path0[1])
            distances.append(d)
        return min(distances)

    test(f("R8,U5,L5,D3\nU7,R6,D4,L4"), 6)
    test(f("R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"), 159)
    test(f("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"), 135)

    fn = open("03/input", 'r')
    values = "\n".join([l.strip() for l in fn])
    return f(values)

def main2():

    def f(wires):

        wires = [w.split(',') for w in wires.split('\n')]

        paths = []
        pathsi = []
        for wire in wires:
            x, y = 0, 0
            path = []
            pathi = []
            step = 0
            for value in wire:
                v = int(value[1:])
                for _v in range(1, v + 1):
                    if "U" in value: y += 1
                    if "R" in value: x += 1
                    if "D" in value: y -= 1
                    if "L" in value: x -= 1
                    step += 1
                    path.append((x, y, step))
                    pathi.append(10**7 * x + y)
            paths.append(path)
            pathsi.append(pathi)

        crosses1 = np.in1d(pathsi[0], pathsi[1])
        crosses1 = np.array(paths[0])[crosses1]

        crosses2 = np.in1d(pathsi[1], pathsi[0])
        crosses2 = np.array(paths[1])[crosses2]

        c2x = array([c[0] for c in crosses2])
        c2y = array([c[1] for c in crosses2])
        lengths = []
        for cross in crosses1:
            select = (c2x == cross[0]) * (c2y == cross[1])
            lengths.append(cross[2] + crosses2[select, 2])

        return min(lengths)[0]

    test(f("R8,U5,L5,D3\nU7,R6,D4,L4"), 30)
    test(f("R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"), 610)
    test(f("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"), 410)

    fn = open("03/input", 'r')
    values = "\n".join([l.strip() for l in fn])
    return f(values)

if __name__ == "__main__":
    fun = main1 if len(sys.argv) == 1 else main2
    solution = fun()
    print(solution)
