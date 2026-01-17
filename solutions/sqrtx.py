# Time:  O(logn)
# Space: O(1)
# Pattern: Binary Search
#
# INTUITION:
# Find largest m where m*m <= x. Binary search on answer space [1, x/2].
# If mid*mid > x, search left. Else search right. Use mid > x/mid to avoid overflow.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1

        return left - 1


