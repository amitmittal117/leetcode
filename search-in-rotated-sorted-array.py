# Time:  O(logn)
# Space: O(1)
# Pattern: Binary Search

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 1. Standard binary search setup
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) / 2

            # 2. If found, return immediately
            if nums[mid] == target:
                return mid
            
            # 3. Key insight: one half is ALWAYS sorted
            #    - Determine which half is sorted, then check if target is in it
            elif (nums[mid] >= nums[left] and nums[left] <= target < nums[mid]) or \
                 (nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])):
                # 3a. Target is in left half
                #     Case 1: Left half sorted AND target in range [left, mid)
                #     Case 2: Right half sorted but target NOT in (mid, right]
                right = mid - 1
            else:
                # 3b. Target is in right half
                left = mid + 1

        # 4. Not found
        return -1
