# Pattern: Math (Prime Factorization)
# INTUITION:
# Copy-paste to get n 'A's. Each "copy all + paste k times" multiplies count by (k+1).
# Minimum steps = sum of prime factors of n.
# E.g., n=12 = 2*2*3 → 2+2+3 = 7 steps.

# Time:  O(sqrt(n))
# Space: O(1)

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        p = 2
        # the answer is the sum of prime factors
        while p**2 <= n:
            while n % p == 0:
                result += p
                n //= p
            p += 1
        if n > 1:
            result += n
        return result

