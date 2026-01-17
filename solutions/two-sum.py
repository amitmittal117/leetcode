# Time:  O(n)
# Space: O(n)
# Pattern: Hash Map
#
# INTUITION:
# For each number, we need its complement (target - num). Instead of searching
# array each time (O(n²)), store seen numbers in hashmap for O(1) lookup.
# As we iterate, check if complement exists. If yes, we found the pair!

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1. Use hashmap to store {number: index}
        lookup = {}
        
        # 2. For each number, check if complement exists
        for i, num in enumerate(nums):
            # 2a. If complement already seen, we found the answer
            if target - num in lookup:
                return [lookup[target - num], i]
            
            # 2b. Store current number for future lookups
            lookup[num] = i


    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            j = target - i
            tmp_nums_start_index = nums.index(i) + 1
            tmp_nums = nums[tmp_nums_start_index:]
            if j in tmp_nums:
                return [nums.index(i), tmp_nums_start_index + tmp_nums.index(j)]


