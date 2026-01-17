# Time:  O(n)
# Space: O(1)
# Pattern: Sliding Window
#
# INTUITION:
# Think of a "window" sliding over the string. We expand it by adding chars
# on the right. When we hit a duplicate, we shrink from the left until valid.
# The trick: use a hashmap to store each char's last position, so we can
# "jump" the left pointer past the duplicate instead of shrinking one by one.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, left = 0, 0
        
        # 1. Use hashmap to store last seen position of each character
        #    - Why hashmap? O(1) lookup to check if char is in current window
        #    - Stores index (not just presence) to know where duplicate is
        lookup = {}
        
        # 2. Expand window by moving right pointer through string
        #    - This is the "sliding" part - right always moves forward
        for right in xrange(len(s)):
            # 3. Handle duplicate found in current window
            #    - If char exists AND its position >= left (in current window)
            #    - We must shrink window from left
            if s[right] in lookup:
                # 3a. Move left pointer past the duplicate
                #     - Why max()? The stored position might be before current left
                #     - Example: "abba" - when we hit second 'a', 'b' is stored but 
                #       left is already past it, so we shouldn't move left backwards
                left = max(left, lookup[s[right]]+1)
            
            # 4. Update character's most recent position
            #    - Always update, even if char was seen before
            lookup[s[right]] = right
            
            # 5. Update result with current window size
            #    - Window size = right - left + 1
            #    - Take max because we want longest
            result = max(result, right-left+1)
        
        return result

