# Time:  O(n)
# Space: O(1)
# Pattern: Tree (BST Property)
#
# INTUITION:
# In BST, LCA is where p and q split (one goes left, one goes right).
# If both < root, go left. If both > root, go right. Otherwise, root is LCA!

class Solution(object):
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        s, b = sorted([p.val, q.val])
        while not s <= root.val <= b:
            # Keep searching since root is outside of [s, b].
            root = root.left if s <= root.val else root.right
        # s <= root.val <= b.
        return root

