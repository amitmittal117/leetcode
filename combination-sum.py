# Time:  O(k * n^k)
# Space: O(k)
# Pattern: Backtracking

class Solution(object):
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        result = []
        self.combinationSumRecu(sorted(candidates), result, 0, [], target)
        return result

    def combinationSumRecu(self, candidates, result, start, intermediate, target):
        # 1. Base case: found a valid combination
        if target == 0:
            result.append(list(intermediate))
        
        # 2. Try each candidate starting from 'start'
        #    - Why start? Avoid duplicates like [2,3] and [3,2]
        #    - While loop + start acts like "for i in range(start, n)"
        while start < len(candidates) and candidates[start] <= target:
            # 2a. CHOOSE: add candidate to current combination
            intermediate.append(candidates[start])
            
            # 2b. EXPLORE: recurse with SAME start index
            #     - Why same? Elements can be reused unlimited times
            #     - Subtract from target to track remaining sum
            self.combinationSumRecu(candidates, result, start, intermediate, target - candidates[start])
            
            # 2c. UNCHOOSE: backtrack
            intermediate.pop()
            
            # 2d. Move to next candidate (no duplicates of this element)
            start += 1
