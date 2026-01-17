# Time:  O(n)
# Space: O(1)
# Pattern: Linked List (Fast/Slow Pointers)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        # Floyd's Cycle Detection (Tortoise and Hare)
        
        # 1. Initialize two pointers at head
        #    - slow moves 1 step at a time
        #    - fast moves 2 steps at a time
        fast, slow = head, head
        
        # 2. Move until fast reaches end OR they meet
        #    - If no cycle: fast hits None
        #    - If cycle: fast will eventually catch slow
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            
            # 2a. If they meet, there's a cycle
            #     - Why must they meet? Fast gains 1 step per iteration
            #     - In a cycle of length k, they meet within k iterations
            if fast is slow:
                return True
        
        # 3. fast reached end - no cycle
        return False
