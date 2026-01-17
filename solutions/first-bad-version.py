# Time:  O(logn)
# Space: O(1)
# Pattern: Binary Search (First True)
#
# INTUITION:
# All versions after first bad are also bad. Binary search for boundary!
# If mid is bad, search left (answer is mid or earlier). If good, search right.
# Classic "find first occurrence" binary search pattern.

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            if isBadVersion(mid): # noqa
                right = mid - 1
            else:
                left = mid + 1
        return left

