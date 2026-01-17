# Time:  O(n)
# Space: O(n)
# Pattern: Hash Set
#
# INTUITION:
# Set removes duplicates. If set size < array size, duplicates exist!
# Alternative: sort and check adjacent elements, but that's O(n log n).

class Solution(object):
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))

