# Time:  O(n)
# Space: O(1)
# Pattern: Linked List (Two Lists Merge)
#
# INTUITION:
# Partition around x: nodes < x before nodes >= x. Create two separate lists
# (smaller and greater), traverse original adding to appropriate list, then join.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        dummySmaller, dummyGreater = ListNode(-1), ListNode(-1)
        smaller, greater = dummySmaller, dummyGreater

        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next

        smaller.next = dummyGreater.next
        greater.next = None

        return dummySmaller.next

