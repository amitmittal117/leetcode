# Time:  O(n)
# Space: O(1)
# Pattern: Dynamic Programming

class Solution(object):
    # @param num, a list of integer
    # @return an integer
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP INSIGHT: At each house, choose max of:
        # - Rob this house + best from 2 houses ago (can't rob adjacent)
        # - Skip this house + keep best so far
        
        # 1. Initialize: last = best ending 2 ago, now = best ending at previous
        #    - Why two variables? Only need last 2 states (space optimized)
        last, now = 0, 0
        
        # 2. For each house, decide: rob it or skip it
        for i in nums:
            # 2a. Recurrence: now = max(skip this house, rob this house)
            #     - skip: keep current best (now)
            #     - rob: add this house value (i) to best from 2 ago (last)
            #     - last becomes old now for next iteration
            last, now = now, max(last + i, now)
        
        return now
