# Time:  O(n)
# Space: O(n)
# Pattern: Dynamic Programming / Bit Manipulation
#
# INTUITION:
# Count of 1s in i = count in (i >> 1) + last bit (i & 1).
# Right shift removes last bit, which we already computed! Build up from 0.
# DP relation: bits[i] = bits[i >> 1] + (i & 1).

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        for i in xrange(1, num + 1):
            # Number of 1's in i = (i & 1) + number of 1's in (i / 2).
            res.append((i & 1) + res[i >> 1])
        return res

    def countBits2(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        s = [0]
        while len(s) <= num:
            s.extend(map(lambda x: x + 1, s))
        return s[:num + 1]


