# Time:  O(n)
# Space: O(k), k is the number of different characters
# Pattern: Sliding Window
#
# INTUITION:
# Expand window until it contains all required chars, then shrink from left
# to find minimum. Track char counts with hashmap. "Remain" tracks how many
# chars still needed. When remain=0, window is valid - try shrinking it.

import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 1. Count required characters and initialize tracking
        #    - count: frequency of each char needed
        #    - remain: total chars still needed to form valid window
        count, remain = collections.Counter(t), len(t)
        i, left, right = 0, -1, -1
        
        # 2. Expand window with right pointer (j)
        for j, c in enumerate(s):
            # 2a. If char is needed (count > 0), decrement remain
            remain -= count[c] > 0
            count[c] -= 1
            
            # 2b. If window doesn't contain all chars yet, keep expanding
            if remain:
                continue
            
            # 3. Shrink window from left while maintaining validity
            #    - While left char is not needed (count < 0), remove it
            while count[s[i]] < 0:
                count[s[i]] += 1
                i += 1
            
            # 4. Update result if this window is smaller
            if right == -1 or j-i+1 < right-left+1:
                left, right = i, j
        
        return s[left:right+1]


# Time:  O(n)
# Space: O(k), k is the number of different characters
class Solution2(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        current_count = [0 for i in xrange(52)]
        expected_count = [0 for i in xrange(52)]

        for char in t:
            expected_count[ord(char) - ord('a')] += 1

        i, count, start, min_width, min_start = 0, 0, 0, float("inf"), 0
        while i < len(s):
            current_count[ord(s[i]) - ord('a')] += 1
            if current_count[ord(s[i]) - ord('a')] <= expected_count[ord(s[i]) - ord('a')]:
                count += 1

            if count == len(t):
                while expected_count[ord(s[start]) - ord('a')] == 0 or \
                      current_count[ord(s[start]) - ord('a')] > expected_count[ord(s[start]) - ord('a')]:
                    current_count[ord(s[start]) - ord('a')] -= 1
                    start += 1

                if min_width > i - start + 1:
                    min_width = i - start + 1
                    min_start = start
            i += 1

        if min_width == float("inf"):
            return ""

        return s[min_start:min_start + min_width]


