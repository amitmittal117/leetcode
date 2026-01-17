# Time:  O(logn)
# Space: O(1)
# Pattern: Binary Search
#
# INTUITION:
# Imagine looking for a word in a dictionary. You don't start from page 1 -
# you open to the middle, see if your word comes before or after, then repeat.
# Each time you eliminate HALF the remaining pages. That's binary search!
# Key insight: sorted data lets us make informed decisions about where to look.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 1. Define search boundaries
        #    - Why both inclusive? We want to check every element including edges
        #    - left=0: start from first element
        #    - right=len-1: end at last element (not len, to avoid out of bounds)
        left, right = 0, len(nums)-1
        
        # 2. Search while range is valid
        #    - Why <=? When left==right, we still have one unchecked element
        #    - If we used <, we'd miss the case where target is at that position
        while left <= right:
            # 2a. Calculate middle index
            #     - Why left + (right-left)//2 instead of (left+right)//2?
            #     - Prevents integer overflow in languages like C++/Java
            #     - In Python it's not an issue, but good practice
            mid = left + (right-left)//2
            
            # 2b. Compare and narrow the search space
            #     - Why eliminate half each time? That's what gives O(logn)
            if nums[mid] > target:
                # Target is smaller, can only be in left half
                right = mid-1
            elif nums[mid] < target:
                # Target is larger, can only be in right half
                left = mid+1
            else:
                # Found it!
                return mid
        
        # 3. Target not found - exhausted all possibilities
        return -1
