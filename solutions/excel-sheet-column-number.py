# Time:  O(n)
# Space: O(1)
# Pattern: Math (Base 26)
#
# INTUITION:
# Excel columns are base-26 numbers. 'A'=1, 'B'=2, ..., 'Z'=26.
# Like decimal: result = result * 26 + digit_value for each character.

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in xrange(len(s)):
            result *= 26
            result += ord(s[i]) - ord('A') + 1
        return result


