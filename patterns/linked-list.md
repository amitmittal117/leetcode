# Linked List Pattern 🔗

## Core Idea
Pointer manipulation on node-based data structures

## When to Use
- In-place list modifications
- Cycle detection
- Merging/reversing lists
- Finding middle element

## Key Techniques
- **Dummy nodes**: Avoid edge cases for head
- **Fast/slow pointers**: Find middle, detect cycles
- **Previous pointer**: For deletion/reversal

## Template

### Dummy Node Pattern
```python
def process_list(head):
    # 1. Create dummy node pointing to head
    #    - Why? Simplifies edge cases (empty list, single node)
    #    - We return dummy.next at the end
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    # 2. Process list
    while current.next:
        # Do something with current.next
        current = current.next
    
    return dummy.next
```

### Build List with Carry (Addition)
```python
def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    # Process both lists digit by digit
    while l1 or l2 or carry:
        val = carry
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next
        
        carry, digit = divmod(val, 10)
        current.next = ListNode(digit)
        current = current.next
    
    return dummy.next
```

### Reverse List
```python
def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next  # Save next
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_temp       # Move current forward
    
    return prev
```

### Find Middle (Fast/Slow)
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # Middle node
```

---

## Problems

| Problem | Difficulty | Key Insight |
|---------|------------|-------------|
| [add-two-numbers.py](file:///c:/Users/amit/Desktop/projects/LeetProject/leetcode/add-two-numbers.py) | Medium | Dummy + carry ✅ |

---

[← Back to Patterns](./README.md)
