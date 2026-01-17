# Time:  O(k), where k is the steps to be happy number
# Space: O(k)
# Pattern: Hash Set / Floyd's Cycle Detection
#
# INTUITION:
# Keep computing sum of digit squares. Either reaches 1 (happy) or loops.
# Detect loop with hash set or Floyd's cycle detection (fast/slow pointers).

class Solution(object):
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        lookup = {}
        while n != 1 and n not in lookup:
            lookup[n] = True
            n = self.nextNumber(n)
        return n == 1

    def nextNumber(self, n):
        new = 0
        for char in str(n):
            new += int(char)**2
        return new

