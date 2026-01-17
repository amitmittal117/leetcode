# Time:  O(1)
# Space: O(1)
# Pattern: Bit Manipulation
#
# INTUITION:
# Powers of 2 in binary have exactly one '1' bit (e.g., 8 = 1000).
# n & (n-1) clears the lowest set bit. If result is 0 and n > 0, it's power of 2!
# Example: 8 & 7 = 1000 & 0111 = 0. But 7 & 6 = 0111 & 0110 = 0110 ≠ 0.

class Solution(object):
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0


class Solution2(object):
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and (n & ~-n) == 0

