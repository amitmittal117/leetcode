# Pattern: Dynamic Programming + Hash Map (Subsequence Counting)
# INTUITION:
# dp[i][d] = count of arithmetic subsequences ending at i with difference d.
# For each pair (j, i): extend all subsequences ending at j with same diff.
# Only count subsequences of length >= 3.

# Time:  O(n^2)
# Space: O(n * d)

import collections


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        dp = [collections.defaultdict(int) for i in xrange(len(A))]
        for i in xrange(1, len(A)):
            for j in xrange(i):
                diff = A[i]-A[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    result += dp[j][diff]
        return result

