# Pattern: Greedy / Bit Parity
# INTUITION:
# A 2-bit character starts with 1 and consumes the next bit.
# Scan backwards from the second-to-last element: count consecutive 1s.
# If that count is even, the last character is a 1-bit (single 0).

# Time:  O(n)
# Space: O(1)


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        parity = 0
        for i in reversed(xrange(len(bits)-1)):
            if bits[i] == 0:
                break
            parity ^= bits[i]
        return parity == 0

