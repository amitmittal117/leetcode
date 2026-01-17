# edit-distance.py
# Time:  O(n * m)
# Space: O(n + m)
# Pattern: Dynamic Programming (2D, Space Optimized)
#
# INTUITION:
# How to transform word1 → word2? At each position, 3 choices: insert, delete, replace.
# dp[i][j] = min operations to transform word1[0:i] → word2[0:j].
# If chars match, no operation needed. Otherwise, take min of 3 operations.
# Space optimized: only need previous row, not entire 2D table.

class Solution(object):
    # @return an integer
    def minDistance(self, word1, word2):
        # Optimization: work with shorter string as columns
        if len(word1) < len(word2):
            return self.minDistance(word2, word1)

        # 1. Initialize: distance[j] = j (need j inserts to match word2[0:j])
        distance = [i for i in xrange(len(word2) + 1)]

        # 2. Fill row by row
        for i in xrange(1, len(word1) + 1):
            pre_distance_i_j = distance[0]  # Save for diagonal
            distance[0] = i  # Need i deletes
            
            for j in xrange(1, len(word2) + 1):
                # 2a. Three options: insert, delete, replace
                insert = distance[j - 1] + 1
                delete = distance[j] + 1
                replace = pre_distance_i_j
                
                # 2b. Replace costs 1 if chars differ
                if word1[i - 1] != word2[j - 1]:
                    replace += 1
                
                pre_distance_i_j = distance[j]  # Save before overwriting
                distance[j] = min(insert, delete, replace)

        return distance[-1]


# Time:  O(n * m)
# Space: O(n * m)
class Solution2(object):
    # @return an integer
    def minDistance(self, word1, word2):
        distance = [[i] for i in xrange(len(word1) + 1)]
        distance[0] = [j for j in xrange(len(word2) + 1)]

        for i in xrange(1, len(word1) + 1):
            for j in xrange(1, len(word2) + 1):
                insert = distance[i][j - 1] + 1
                delete = distance[i - 1][j] + 1
                replace = distance[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    replace += 1
                distance[i].append(min(insert, delete, replace))

        return distance[-1][-1]

