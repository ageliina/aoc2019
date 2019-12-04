#!/usr/bin/env python3
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi

"""
aoc2019.4
"""

from collections import Counter
print(sum(1 for i in map(str, range(284639, 748759 + 1)
          if sorted(i) == list(i) and 2 in Counter(i).values()))
