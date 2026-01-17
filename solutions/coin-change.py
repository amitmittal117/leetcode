# Time:  O(n * k), n is the number of coins, k is the amount of money
# Space: O(k)
# Pattern: Dynamic Programming (Bottom-up, Unbounded Knapsack variant)
#
# INTUITION:
# For each amount from 0 to target, ask: "what's the minimum coins to make this?"
# For amount X, try each coin: if I use this coin, I need 1 + dp[X-coin].
# Build up from amount 0 (needs 0 coins) to target. Unreachable amounts stay ∞.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # DP INSIGHT: For each amount, find minimum coins needed
        # - dp[i] = minimum coins to make amount i
        # - dp[i] = min(dp[i], dp[i-coin] + 1) for each coin
        
        # 1. Initialize DP array with "infinity"
        #    - Why infinity? Marks amounts we can't make (yet)
        #    - Why 0x7fffffff instead of float("inf")? Faster in Python
        INF = 0x7fffffff
        dp = [INF] * (amount + 1)
        
        # 2. Base case: 0 coins needed to make amount 0
        dp[0] = 0
        
        # 3. Build solution bottom-up
        #    - For each amount we can already make...
        for i in xrange(amount + 1):
            if dp[i] != INF:  # Only process reachable amounts
                # 3a. Try adding each coin denomination
                for coin in coins:
                    # 3b. If adding this coin stays within target amount
                    if i + coin <= amount:
                        # 3c. Update if this path uses fewer coins
                        #     - dp[i+coin]: current best for amount i+coin
                        #     - dp[i] + 1: using 1 more coin from amount i
                        dp[i + coin] = min(dp[i + coin], dp[i] + 1)
        
        # 4. Return result
        #    - If still infinity, amount is impossible to make
        return dp[amount] if dp[amount] != INF else -1
