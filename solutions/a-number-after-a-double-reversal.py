# Pattern: Math (Trailing Zeros)
# INTUITION:
# Double reversal loses trailing zeros. num == reversed(reversed(num)) only if
# num has no trailing zeros OR num is 0. Check: num == 0 or num % 10 != 0.

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num == 0 or num%10
