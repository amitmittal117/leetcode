# Pattern: Prefix Sum (Counting Zero Crossings)
# INTUITION:
# Ant starts at 0, moves by nums[i] each step.
# Count how many times position returns to 0 (prefix sum = 0).

# ant-on-the-boundary.py
# Time:  O(n)
# Space: O(1)

# prefix sum
class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = curr = 0
        for x in nums:
            curr += x
            if curr == 0:
                result += 1
        return result
