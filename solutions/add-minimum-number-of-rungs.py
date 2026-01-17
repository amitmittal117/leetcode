# Pattern: Greedy / Math
# INTUITION:
# For each gap between consecutive rungs (or ground to first rung),
# calculate how many intermediate rungs are needed: ceil(gap / dist) - 1.
# Sum these values for all gaps.

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+(b-1))//b

        result = prev = 0
        for curr in rungs:
            result += ceil_divide(curr-prev, dist)-1
            prev = curr
        return result
