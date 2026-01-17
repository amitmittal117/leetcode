# Time:  O(logn)
# Space: O(1)
# Pattern: Dynamic Programming (Matrix Exponentiation - Advanced)

import itertools


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Advanced approach using matrix exponentiation
        # - This achieves O(log n) by exploiting Fibonacci matrix property
        # - For learning DP, see Solution2 below (simpler, more intuitive)
        def matrix_expo(A, K):
            result = [[int(i==j) for j in xrange(len(A))] \
                      for i in xrange(len(A))]
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K /= 2
            return result

        def matrix_mult(A, B):
            ZB = zip(*B)
            return [[sum(a*b for a, b in itertools.izip(row, col)) \
                     for col in ZB] for row in A]

        T = [[1, 1],
             [1, 0]]
        return matrix_mult([[1,  0]], matrix_expo(T, n))[0][0]  # [a0, a(-1)] * T^n


# Time:  O(n)
# Space: O(1)
# Pattern: Dynamic Programming (Bottom-up, Space Optimized)

class Solution2(object):
    """
    :type n: int
    :rtype: int
    """
    def climbStairs(self, n):
        # DP INSIGHT: At each step, you can take 1 or 2 stairs
        # - ways(n) = ways(n-1) + ways(n-2)
        # - This is exactly the Fibonacci sequence!
        
        # 1. Initialize base cases
        #    - prev = ways to reach step 0 (standing at ground) = 1 way (do nothing)
        #    - current = ways to reach step 1 = 1 way (take one step)
        prev, current = 0, 1
        
        # 2. Build solution bottom-up
        #    - Why this order? We only need previous 2 values, not entire array
        #    - Space optimization: O(1) instead of O(n) DP table
        for i in xrange(n):
            # 2a. Current becomes new previous
            # 2b. New current = old current + old prev (Fibonacci recurrence)
            #     - Why? To reach step i, you either:
            #       - Came from step i-1 (took 1 step) OR
            #       - Came from step i-2 (took 2 steps)
            prev, current = current, prev + current,
        
        return current

