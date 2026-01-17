# Time:  O(n)
# Space: O(1)
# Pattern: Greedy
#
# INTUITION:
# If total gas >= total cost, solution exists. Track current tank: if goes negative,
# start point can't be before current position. Start from next station.

class Solution(object):
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        start, total_sum, current_sum = 0, 0, 0
        for i in xrange(len(gas)):
            diff = gas[i] - cost[i]
            current_sum += diff
            total_sum += diff
            if current_sum < 0:
                start = i + 1
                current_sum = 0
        if total_sum >= 0:
            return start

        return -1

