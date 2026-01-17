# Pattern: Math (Rounding)
# INTUITION:
# Round purchase to nearest 10 (round up on .5). Subtract from 100.
# Adding 5 before integer division by 10 achieves "round half up".

# Time:  O(1)
# Space: O(1)

# math
class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        return 100-(purchaseAmount+5)//10*10
