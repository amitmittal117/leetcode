# Time:  O(n)
# Space: O(1)
# Pattern: Two Pointers
#
# INTUITION:
# Two pointers at both ends, swap and move inward until they meet.
# Simple and elegant O(n) time, O(1) space in-place reversal.

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
