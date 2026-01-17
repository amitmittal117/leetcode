# Time:  O(n^2)
# Space: O(1)
# Pattern: Matrix Manipulation
#
# INTUITION:
# Rotate 90° clockwise = transpose + reverse each row. Or here: anti-diagonal
# mirror + horizontal mirror. Each swap moves element to its rotated position.
# In-place, O(1) space. Key: break rotation into two mirror operations.

class Solution(object):
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)

        # 1. Anti-diagonal mirror (swap matrix[i][j] with matrix[n-1-j][n-1-i])
        for i in xrange(n):
            for j in xrange(n - i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]

        # 2. Horizontal mirror (swap top and bottom rows)
        for i in xrange(n / 2):
            for j in xrange(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

        return matrix


# Time:  O(n^2)
# Space: O(n^2)
class Solution2(object):
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        return [list(reversed(x)) for x in zip(*matrix)]

