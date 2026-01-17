# Time:  O(logn)
# Space: O(1)
# Pattern: Binary Search
#
# INTUITION:
# Find index where target would be inserted to keep array sorted.
# Binary search: find leftmost position where nums[i] >= target.
# If found, return index. If not, left pointer ends at insert position.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left


