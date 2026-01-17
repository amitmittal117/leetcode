# Time:  O(m * n), m is the number of nodes of s, n is the number of nodes of t
# Space: O(h), h is the height of s
# Pattern: Tree (Recursion)
#
# INTUITION:
# Check if t is subtree of s. At each node of s, check if subtrees match.
# isSame(x,y): are trees identical? Then traverse s checking isSame at each node.

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSame(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            return x.val == y.val and \
                   isSame(x.left, y.left) and \
                   isSame(x.right, y.right)

        def preOrderTraverse(s, t):
            return s != None and \
                   (isSame(s, t) or \
                    preOrderTraverse(s.left, t) or \
                    preOrderTraverse(s.right, t))

        return preOrderTraverse(s, t)

