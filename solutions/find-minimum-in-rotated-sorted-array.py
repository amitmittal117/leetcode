# Time:  O(logn)
# Space: O(1)
# Pattern: Binary Search
#
# INTUITION:
# In rotated sorted array, minimum is at the "pivot" - where largest meets smallest.
# Binary search: compare mid with rightmost element. If mid > right, min is in
# right half (we haven't passed pivot yet). Otherwise, min is in left half or mid.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)
        target = nums[-1]

        while left < right:
            mid = left + (right - left) / 2

            if nums[mid] <= target:
                right = mid
            else:
                left = mid + 1

        return nums[left]


class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right and nums[left] >= nums[right]:
            mid = left + (right - left) / 2

            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


