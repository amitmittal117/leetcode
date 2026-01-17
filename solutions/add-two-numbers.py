# Time:  O(n)
# Space: O(1)
# Pattern: Linked List
#
# INTUITION:
# Just like adding numbers on paper! Start from rightmost digit (head of list),
# add digits + carry, keep the ones place, carry the tens. The dummy node trick
# avoids special handling for the first node. Process until both lists AND
# carry are exhausted.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 1. Create dummy head node
        #    - Why dummy? Simplifies edge cases when building result list
        #    - No need for special logic to initialize head vs append
        #    - We'll return dummy.next at the end
        dummy = ListNode(0)
        current, carry = dummy, 0

        # 2. Process both lists digit by digit
        #    - Why "or"? Lists may have different lengths (e.g., 99 + 1)
        #    - Continue until both lists are exhausted
        while l1 or l2:
            # 2a. Start with carry from previous digit
            val = carry
            
            # 2b. Add digit from l1 if available
            if l1:
                val += l1.val
                l1 = l1.next
            
            # 2c. Add digit from l2 if available
            if l2:
                val += l2.val
                l2 = l2.next
            
            # 2d. Extract digit and carry using divmod
            #     - divmod(15, 10) → (1, 5): carry=1, digit=5
            #     - Why divmod? Clean way to get both values at once
            carry, val = divmod(val, 10)
            
            # 2e. Create new node and advance
            current.next = ListNode(val)
            current = current.next

        # 3. Handle remaining carry
        #    - Example: 99 + 1 = 100, final carry of 1 becomes new node
        if carry == 1:
            current.next = ListNode(1)

        return dummy.next
