# Time:  O(n)
# Space: O(1)
# Pattern: Bit Manipulation / Math
#
# INTUITION:
# XOR method: a ^ a = 0, a ^ 0 = a. XOR all numbers 0 to n with array.
# All present numbers cancel out, leaving the missing one!
# Or use math: expected_sum - actual_sum = missing number.

import operator

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums,
                      reduce(operator.xor, xrange(len(nums) + 1)))


class Solution2(object):
    def missingNumber(self, nums):
        return sum(xrange(len(nums)+1)) - sum(nums)

