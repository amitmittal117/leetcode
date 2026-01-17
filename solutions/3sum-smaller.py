# Pattern: Two Pointers (k-Sum Variant)
# INTUITION:
# Count triplets with sum < target. Sort the array.
# Fix the largest element k, use two pointers i, j for remaining pairs.
# If sum < target, all pairs (i, i+1..j) are valid → add (j - i), then move i.

# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumSmaller(self, nums, target):
        nums.sort()
        n = len(nums)

        count, k = 0, 2
        while k < n:
            i, j = 0, k - 1
            while i < j:  # Two Pointers, linear time.
                if nums[i] + nums[j] + nums[k] >= target:
                    j -= 1
                else:
                    count += j - i
                    i += 1
            k += 1

        return count

