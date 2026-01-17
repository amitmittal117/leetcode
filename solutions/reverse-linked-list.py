# Time:  O(n)
# Space: O(1)
# Pattern: Linked List
#
# INTUITION:
# Reversal = changing each arrow's direction. For each node: save next, point to prev,
# move forward. Need 3 pointers: prev (builds reversed list), curr (current node),
# next (saved so we don't lose it). At end, prev is new head.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

# Iterative solution.
class Solution(object):
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        # 1. Create dummy node to collect reversed nodes
        #    - Why dummy? Simplifies building the reversed list
        #    - Acts as a "collector" for nodes in reverse order
        dummy = ListNode(float("-inf"))
        
        # 2. Process each node: detach from original, attach to reversed
        while head:
            # 2a. Triple assignment does three things simultaneously:
            #     - dummy.next = head: attach current node to front of reversed list
            #     - head.next = dummy.next: link current to previous reversed nodes
            #     - head = head.next: move to next node in original list
            #     Order matters! Python evaluates right side first, then assigns
            dummy.next, head.next, head = head, dummy.next, head.next
        
        return dummy.next


# Time:  O(n)
# Space: O(n)
# Recursive solution.
class Solution2(object):
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        [begin, end] = self.reverseListRecu(head)
        return begin

    def reverseListRecu(self, head):
        if not head:
            return [None, None]

        [begin, end] = self.reverseListRecu(head.next)

        if end:
            end.next = head
            head.next = None
            return [begin, head]
        else:
            return [head, head]

