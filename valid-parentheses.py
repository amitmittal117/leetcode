# Time:  O(n)
# Space: O(n)
# Pattern: Stack

class Solution(object):
    # @return a boolean
    def isValid(self, s):
        # 1. Initialize stack and mapping of open to close brackets
        #    - Why stack? LIFO property matches nested bracket structure
        #    - Most recent open bracket must match first close bracket
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        
        # 2. Process each character
        for parenthese in s:
            if parenthese in lookup:
                # 2a. Opening bracket: push to stack
                #     - We'll match it later when we find closing
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                # 2b. Closing bracket: must match top of stack
                #     - Empty stack = no opening to match
                #     - Mismatch = invalid sequence
                return False
        
        # 3. All brackets must be matched (stack empty)
        #    - If stack not empty, we have unmatched opening brackets
        return len(stack) == 0
