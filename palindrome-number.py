# Time:  O(1)
# Space: O(1)
# Pattern: Math
#
# INTUITION:
# Reverse the number and compare. Negative numbers can't be palindromes.
# Build reverse digit by digit: reverse = reverse * 10 + num % 10.

class Solution(object):
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        copy, reverse = x, 0

        while copy:
            reverse *= 10
            reverse += copy % 10
            copy //= 10

        return x == reverse

