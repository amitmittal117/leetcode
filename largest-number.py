# Time:  O(nlogn)
# Space: O(1)
# Pattern: Sorting (Custom Comparator)
#
# INTUITION:
# Form largest number by concatenating. Key: compare a+b vs b+a as strings.
# If "9" + "34" = "934" > "349" = "34" + "9", then 9 should come first.

class Solution(object):
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = [str(x) for x in num]
        num.sort(cmp=lambda x, y: cmp(y + x, x + y))
        largest = ''.join(num)
        return largest.lstrip('0') or '0'

