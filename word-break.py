# Time:  O(n * l^2)
# Space: O(n)
# Pattern: Dynamic Programming

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)

        # 1. Optimization: find max word length to limit inner loop
        #    - No need to check substrings longer than longest word
        max_len = 0
        for string in wordDict:
            max_len = max(max_len, len(string))

        # 2. DP: can_break[i] = can we segment s[0:i]?
        #    - Base case: can_break[0] = True (empty string)
        can_break = [False for _ in xrange(n + 1)]
        can_break[0] = True
        
        # 3. For each position, check if we can reach it
        for i in xrange(1, n + 1):
            # 3a. Try all possible last word lengths (up to max_len)
            for l in xrange(1, min(i, max_len) + 1):
                # 3b. If position i-l is reachable AND s[i-l:i] is a word
                #     then position i is reachable
                if can_break[i-l] and s[i-l:i] in wordDict:
                    can_break[i] = True
                    break  # Found one valid segmentation, move on

        return can_break[-1]
