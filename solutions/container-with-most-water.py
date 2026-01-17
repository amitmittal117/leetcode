# Time:  O(n)
# Space: O(1)
# Pattern: Two Pointers
#
# INTUITION:
# Water container = width × height (shorter wall). Start with widest possible
# container (both ends). To find more water, we need more height since width
# only shrinks. Moving the taller wall can't help (limited by shorter one),
# so always move the shorter wall hoping to find a taller one.

class Solution(object):
    # @return an integer
    def maxArea(self, height):
        # 1. Initialize pointers at both ends and track max area
        #    - Why start at ends? Maximize width first, then optimize height
        max_area, i, j = 0, 0, len(height) - 1
        
        # 2. Move pointers inward until they meet
        while i < j:
            # 2a. Calculate current area: min(heights) * width
            #     - Why min? Water can only rise to shorter wall
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            
            # 2b. Move the pointer with shorter height
            #     - Why shorter? Moving taller one can only decrease area
            #       (width decreases, height limited by shorter wall anyway)
            #     - Moving shorter one might find a taller wall
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return max_area
