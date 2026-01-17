# Time : O(32)
# Space: O(1)
# Pattern: Bit Manipulation
#
# INTUITION:
# Reverse 32-bit integer: swap halves, then quarters, eighths, etc. (divide & conquer).
# Or simple loop: extract rightmost bit of n, shift into result from left.
# Both O(32) = O(1). First method uses clever bitmasks for parallel swaps.

class Solution(object):
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


# Time : O(logn) = O(32)
# Space: O(1)
class Solution2(object):
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in xrange(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

