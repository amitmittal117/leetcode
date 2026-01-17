# Pattern: Array (Running Length Tracking)
# INTUITION:
# Find maximum k such that two adjacent strictly increasing subarrays of length k exist.
# Track current and previous increasing lengths.
# Max k = max(curr//2, min(prev, curr)).

# adjacent-increasing-subarrays-detection-ii.py
# adjacent-increasing-subarrays-detection-ii.py
# Time:  O(n)
# Space: O(1)

# array
class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        curr, prev = 1, 0
        for i in xrange(len(nums)-1):
            if nums[i] < nums[i+1]:
                curr += 1
            else:
                prev = curr
                curr = 1
            result = max(result, curr//2, min(prev, curr))
        return result
