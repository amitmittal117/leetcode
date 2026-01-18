# Pattern: Dynamic Programming (String Matching)
# INTUITION:
# Find positions where s1[i] != s2[i]. Pair them to flip.
# Two options: pair adjacent diff positions (cost = distance*2), or pair any two (cost = x).
# DP tracks min cost, ensuring even number of diffs (parity check).

# Time:  O(n)
# Space: O(1)

# dp
class Solution(object):
    def minOperations(self, s1, s2, x):
        """
        :type s1: str
        :type s2: str
        :type x: int
        :rtype: int
        """
        parity = curr = prev = 0
        j = -1
        for i in xrange(len(s1)):
            if s1[i] == s2[i]:
                continue
            curr, prev = min(curr+x, prev+(i-j)*2 if j != -1 else float("inf")), curr
            j = i
            parity ^= 1
        return curr//2 if parity == 0 else -1
