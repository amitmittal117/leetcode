# Time:  O(n)
# Space: O(1)
# Pattern: Linked List (Pointer Manipulation)
#
# INTUITION:
# Group odd-positioned nodes together, then even-positioned. Keep two lists
# (odd and even), link even list to end of odd list. O(1) space!

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            odd_tail, cur = head, head.next
            while cur and cur.next:
                even_head = odd_tail.next
                odd_tail.next = cur.next
                odd_tail = odd_tail.next
                cur.next = odd_tail.next
                odd_tail.next = even_head
                cur = cur.next
        return head

