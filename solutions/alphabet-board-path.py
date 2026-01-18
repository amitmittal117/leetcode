# Pattern: String / Simulation (Grid Navigation)
# INTUITION:
# Alphabet board is a 5x5+1 grid. Calculate row/col for each character.
# Move U/L before D/R to avoid going out of bounds (special case for 'z').
# Move step by step from current position to target.

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        x, y = 0, 0
        result = []
        for c in target:
            y1, x1 = divmod(ord(c)-ord('a'), 5)
            result.append('U' * max(y-y1, 0))
            result.append('L' * max(x-x1, 0))
            result.append('R' * max(x1-x, 0))
            result.append('D' * max(y1-y, 0))
            result.append('!')
            x, y = x1, y1
        return "".join(result)
