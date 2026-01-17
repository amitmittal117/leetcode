# Time:  O(n)
# Space: O(n)
# Pattern: Stack (Monotonic Stack - Circular)
#
# INTUITION:
# Like next-greater-element-i, but array is circular. Trick: iterate 2x array
# using modulo to wrap around. Process from right, stack holds potential answers.

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result, stk = [0] * len(nums), []
        for i in reversed(xrange(2*len(nums))):
            while stk and stk[-1] <= nums[i % len(nums)]:
                stk.pop()
            result[i % len(nums)] = stk[-1] if stk else -1
            stk.append(nums[i % len(nums)])
        return result

