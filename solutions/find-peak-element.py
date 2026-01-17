# Time:  O(logn)
# Space: O(1)
# Pattern: Binary Search
#
# INTUITION:
# A peak exists - array rises then falls (or vice versa). Binary search!
# If mid < mid+1, we're on rising slope - peak is to the right.
# If mid > mid+1, we're on falling slope - peak is at mid or left.

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left


