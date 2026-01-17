# Time:  O(n)
# Space: O(1)
# Pattern: Three Pointers (Dutch National Flag)
#
# INTUITION:
# Sort 0s, 1s, 2s in one pass without counting. Three pointers: left (0s boundary),
# right (2s boundary), current. If 0: swap to left. If 2: swap to right.
# If 1: just move on. Classic Dijkstra's Dutch National Flag algorithm.

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def triPartition(nums, target):
            i, left, right = 0, 0, len(nums)-1
            while i <= right:
                if nums[i] > target:
                    nums[i], nums[right] = nums[right], nums[i]
                    right -= 1
                else:
                    if nums[i] < target:
                        nums[left], nums[i] = nums[i], nums[left]
                        left += 1
                    i += 1

        triPartition(nums, 1)
