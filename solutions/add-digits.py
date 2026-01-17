# Pattern: Math (Digital Root)
# INTUITION:
# Repeatedly sum digits until single digit. This is the "digital root".
# Formula: dr(n) = 1 + (n - 1) % 9 for n > 0, else 0.
# Based on the property that n ≡ digit_sum(n) (mod 9).

# add-digits.py
# Time:  O(1)
# Space: O(1)

class Solution(object):
    """
    :type num: int
    :rtype: int
    """
    def addDigits(self, num):
        return (num - 1) % 9 + 1 if num > 0 else 0

