# Dynamic Programming Pattern 📊

## Core Idea
Break problem into overlapping subproblems, store solutions to avoid recomputation

## When to Use
- Optimization problems (min/max cost, max profit)
- Counting problems (number of ways)
- Decision problems (is it possible?)
- Problems with optimal substructure

## Approaches
- **Top-down (Memoization)**: Recursive with cache
- **Bottom-up (Tabulation)**: Iterative, build from base cases

## Template

### Bottom-up (1D array)
```python
def dp_template(n):
    # 1. Define state: dp[i] = answer for subproblem of size i
    dp = [0] * (n + 1)
    
    # 2. Base case
    dp[0] = base_value
    
    # 3. Fill table (order matters - dependencies first)
    for i in range(1, n + 1):
        # Transition: dp[i] depends on smaller subproblems
        dp[i] = some_function(dp[i-1], dp[i-2], ...)
    
    # 4. Return answer
    return dp[n]
```

### Fibonacci Pattern (Space Optimized)
```python
def climbing_stairs(n):
    # Only need last 2 values, not entire array
    prev, current = 0, 1
    
    for i in range(n):
        prev, current = current, prev + current
    
    return current
```

### Unbounded Knapsack (Coin Change)
```python
def coin_change(coins, amount):
    # dp[i] = minimum coins for amount i
    INF = float('inf')
    dp = [INF] * (amount + 1)
    dp[0] = 0  # Base: 0 coins for amount 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != INF:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != INF else -1
```

### Top-down with Memoization
```python
from functools import lru_cache

def solve(n):
    @lru_cache(maxsize=None)
    def dp(i):
        # Base case
        if i <= 1:
            return base_value
        
        # Recursive case with memoization
        return some_function(dp(i-1), dp(i-2))
    
    return dp(n)
```

## Common DP Categories
1. **Linear DP**: dp[i] depends on dp[i-1], dp[i-2]
2. **Knapsack**: Include/exclude items with capacity
3. **Interval DP**: dp[i][j] for range [i, j]
4. **Grid DP**: dp[i][j] for cell (i, j)
5. **String DP**: LCS, edit distance

---

## Problems

| Problem | Difficulty | Key Insight |
|---------|------------|-------------|
| [climbing-stairs](../solutions/climbing-stairs.py) | Easy | Fibonacci pattern ✅ |
| [coin-change](../solutions/coin-change.py) | Medium | Unbounded knapsack ✅ |
| [house-robber](../solutions/house-robber.py) | Medium | Include/exclude decision ✅ |
| [longest-increasing-subsequence](../solutions/longest-increasing-subsequence.py) | Medium | 1D DP + binary search ✅ |
| [edit-distance](../solutions/edit-distance.py) | Medium | 2D string DP ✅ |
| [unique-paths](../solutions/unique-paths.py) | Medium | Grid DP / Math ✅ |
| [decode-ways](../solutions/decode-ways.py) | Medium | String parsing DP ✅ |
| [word-break](../solutions/word-break.py) | Medium | Prefix matching DP ✅ |
| [2-keys-keyboard](../solutions/2-keys-keyboard.py) | Medium | Prime factorization ✅ |
| [4-keys-keyboard](../solutions/4-keys-keyboard.py) | Medium | Optimal copy-paste ✅ |

---

[← Back to Patterns](./README.md)
