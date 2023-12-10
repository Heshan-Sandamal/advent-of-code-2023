"""After waiting for sometime for the answer from the brute force approach I did a small analysis on why its not giving the answer
Problem is, when element A element find Z element, then after some time it again comes to the same Z element & cycle continues

Used puzzle-1 answer to calculate the cycle sizes for each A node.

start , end , cycle-size

PBA -> RGZ -> 20093 -> RGZ -> 20093
LSA -> VQZ -> 12169 -> VQZ -> 12169
VSA -> BLZ -> 20093 -> BLZ -> 13301
QVA -> XSZ -> 20093 -> XSZ -> 20659
AAA -> ZZZ -> 16697 -> ZZZ -> 16697
VKA -> KKZ -> 17263 -> KKZ -> 17263

This continues...
Which means,
All this will be in the particular Z element when the count equals the least common multiplier of cycle length

"""

import math
print(math.lcm(20093, 12169, 13301, 20659, 16697, 17263))
