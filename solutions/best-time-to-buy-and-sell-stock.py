# Time:  O(n)
# Space: O(1)
# Pattern: Greedy / Kadane's variant
#
# INTUITION:
# To maximize profit: buy at lowest price BEFORE you sell. Track min price seen
# so far as you scan. At each price, calculate potential profit if you sold today.
# Keep track of max profit. One pass, O(1) space - classic greedy!

class Solution(object):
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        # 1. Track min price seen and max profit possible
        max_profit, min_price = 0, float("inf")
        
        # 2. For each day's price
        for price in prices:
            # 2a. Update min price if today is cheaper
            min_price = min(min_price, price)
            
            # 2b. Calculate profit if we sold today, update max
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
