# Pattern: Math (Combinatorics / Parity)
# INTUITION:
# Alice wins when total flowers is odd. Count pairs (x, y) where x+y is odd.
# This happens when one is odd and one is even. Result = (n*m)//2.

# Time:  O(1)
# Space: O(1)

# combinatorics
class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        return (n*m)//2
