# jump-game.py
# Time:  O(n)
# Space: O(1)
# Pattern: Greedy
#
# INTUITION:
# Instead of simulating all jumps, track the FURTHEST index we can reach.
# At each position, update max reachable. If current index > reachable, we're stuck.
# If we can reach or pass the last index, return True. Pure greedy, one pass!

class Solution(object):
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # 1. Track furthest reachable index
        reachable = 0
        
        # 2. For each position, update reachable
        for i, length in enumerate(A):
            # 2a. If current position is beyond reachable, we're stuck
            if i > reachable:
                break
            
            # 2b. Update furthest we can reach from here
            reachable = max(reachable, i + length)
        
        # 3. Can we reach the end?
        return reachable >= len(A) - 1
