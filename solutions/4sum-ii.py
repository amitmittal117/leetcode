# Pattern: Hash Map (Meet in the Middle)
# INTUITION:
# Split 4 arrays into two pairs. Store all (A[i]+B[j]) sums in a Counter.
# For each (C[k]+D[l]), look up -(C[k]+D[l]) in the map. Sum counts.
# Reduces O(n^4) brute force to O(n^2).

# 4sum-ii.py
# Time:  O(n^2)
# Space: O(n^2)

import collections


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        A_B_sum = collections.Counter(a+b for a in A for b in B)
        return sum(A_B_sum[-c-d] for c in C for d in D)

