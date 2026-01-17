# Time:  O(n)
# Space: O(1)
# Pattern: Linked List

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 1. Create dummy node and pointer
        #    - Why dummy? Avoids edge case handling for head
        #    - curr builds the result, dummy.next is the answer
        curr = dummy = ListNode(0)
        
        # 2. Compare and pick smaller element each iteration
        #    - Why while both exist? Need both to compare
        while l1 and l2:
            if l1.val < l2.val:
                # 2a. l1 is smaller, attach it
                curr.next = l1
                l1 = l1.next
            else:
                # 2b. l2 is smaller (or equal), attach it
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        # 3. Attach remaining elements (one list might be longer)
        #    - "l1 or l2" gives whichever is not None
        curr.next = l1 or l2
        
        return dummy.next
