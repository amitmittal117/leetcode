# Time:  O(n^2)
# Space: O(1)
# Pattern: Two Pointers
#
# INTUITION:
# Finding three numbers that sum to 0 seems like O(n³) - try all triplets.
# But if we SORT first, we can be smarter: fix one number, then use two pointers
# to find a pair that sums to its negative. Sorting costs O(n log n), but
# lets us use the "squeeze" technique - if sum too small, move left pointer right;
# if sum too big, move right pointer left. This reduces O(n³) to O(n²).

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        # 1. Sort the array
        #    - Why sort? Enables two-pointer technique (need ordered data)
        #    - Also helps skip duplicates easily (same values are adjacent)
        nums.sort()
        
        # 2. Fix one element and find pairs that sum to its negative
        #    - Why iterate in reverse? Personal preference, works forward too
        #    - Why start at index 2? Need at least 3 elements (indices 0,1,2)
        for i in reversed(xrange(2, len(nums))):
            # 2a. Skip duplicate values for the fixed element
            #     - Why? Avoid duplicate triplets in result
            #     - nums[i] == nums[i+1] means we already processed this value
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                continue
            
            # 2b. The problem becomes: find two numbers that sum to -nums[i]
            target = -nums[i]
            
            # 2c. Two pointer search in the remaining (sorted) subarray
            #     - left starts at beginning, right at position before i
            left, right = 0, i-1
            
            while left < right:
                # 2d. Compare current sum with target
                if nums[left]+nums[right] < target:
                    # Sum too small - need larger value
                    # Why move left? Left pointer has smaller values
                    left += 1
                elif nums[left]+nums[right] > target:
                    # Sum too big - need smaller value
                    # Why move right? Right pointer has larger values
                    right -= 1
                else:
                    # Found a valid triplet!
                    result.append([nums[left], nums[right], nums[i]])
                    
                    # 2e. Move both pointers and skip duplicates
                    #     - Must skip duplicates to avoid duplicate triplets
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        
        return result



# Time:  O(n^2)
# Space: O(1)
class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1
        return result

