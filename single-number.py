# Time:  O(n)
# Space: O(1)
# Pattern: Bit Manipulation
#
# INTUITION:
# Every number appears twice except one. XOR magic: a ^ a = 0, a ^ 0 = a.
# XOR all numbers together - pairs cancel out, leaving the single number!

import operator
from functools import reduce

class Solution(object):
    """
    :type nums: List[int]
    :rtype: int
    """
    def singleNumber(self, A):
        return reduce(operator.xor, A)

