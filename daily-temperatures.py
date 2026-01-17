# Time:  O(n)
# Space: O(n)
# Pattern: Stack (Monotonic Stack)
#
# INTUITION:
# For each day, we want "next warmer day". Brute force: for each day, look ahead.
# Monotonic stack trick: keep indices of unresolved (no warmer yet) days in stack.
# When we find a warmer day, pop all colder days from stack and record the answer.

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # 1. Initialize result array and monotonic stack
        #    - Stack stores INDICES (not values) of unresolved days
        #    - Monotonic: temperatures of indices in stack are decreasing
        result = [0] * len(temperatures)
        stk = []
        
        # 2. Process each day
        for i in xrange(len(temperatures)):
            # 2a. Pop all days that found a warmer day (today)
            #     - While stack not empty AND today is warmer than top
            while stk and \
                  temperatures[stk[-1]] < temperatures[i]:
                # 2b. Calculate days until warmer
                idx = stk.pop()
                result[idx] = i - idx
            
            # 2c. Push today - we'll find its warmer day later
            stk.append(i)
        
        # 3. Any remaining in stack = no warmer day (already 0)
        return result
