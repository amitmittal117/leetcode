# Time:  O(nlogn)
# Space: O(1)
# Pattern: Intervals / Sorting
#
# INTUITION:
# After sorting by start time, overlapping intervals are adjacent. Scan through:
# if current interval overlaps with last result (start <= last.end), merge them
# by extending end. Otherwise, it's a new non-overlapping interval.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 1. Sort by start time
        intervals.sort()
        result = []
        
        # 2. Process each interval
        for interval in intervals:
            # 2a. If no result or no overlap, add as new interval
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                # 2b. Overlap! Extend the end of last interval
                result[-1][1] = max(result[-1][1], interval[1])
        
        return result

