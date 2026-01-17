# Time:  O(m + n)
# Space: O(m + n)
# Pattern: Stack (Monotonic Stack)
#
# INTUITION:
# For each element, find next greater to the right. Monotonic stack: process
# elements, pop smaller ones (they found their next greater), push current.
# Store results in hashmap for O(1) lookup.

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stk, lookup = [], {}
        for num in nums:
            while stk and num > stk[-1]:
                lookup[stk.pop()] = num
            stk.append(num)
        while stk:
            lookup[stk.pop()] = -1
        return map(lambda x : lookup[x], findNums)

