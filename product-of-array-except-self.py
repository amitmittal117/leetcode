# Time:  O(n)
# Space: O(1)
# Pattern: Prefix/Suffix Products
#
# INTUITION:
# Product except self = (all elements left of i) × (all elements right of i).
# Two passes: first pass builds left products, second pass multiplies by right
# products on the fly. No division needed, O(1) extra space (output doesn't count).

class Solution(object):
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        if not nums:
            return []

        # 1. First pass: build left products
        #    left_product[i] = product of all nums[0:i]
        left_product = [1 for _ in xrange(len(nums))]
        for i in xrange(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        # 2. Second pass: multiply by right products
        #    right_product accumulates product of all nums[i+1:]
        right_product = 1
        for i in xrange(len(nums) - 2, -1, -1):
            right_product *= nums[i + 1]
            left_product[i] = left_product[i] * right_product


