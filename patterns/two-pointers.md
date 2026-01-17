# Two Pointers Pattern 👆👆

## Core Idea
Use two pointers to reduce nested loops from O(n²) to O(n)

## When to Use
- Sorted array operations
- Finding pairs/triplets with sum conditions
- Comparing from both ends
- Partitioning arrays

## Builds On
- Binary Search (same divide & conquer thinking)

## Template

```python
def two_pointers(nums, target):
    # 1. Sort if needed (many two-pointer problems require sorted input)
    nums.sort()
    
    # 2. Initialize pointers at opposite ends
    left, right = 0, len(nums) - 1
    
    # 3. Move pointers based on comparison
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum < target:
            # Sum too small - need larger value
            left += 1
        elif current_sum > target:
            # Sum too big - need smaller value  
            right -= 1
        else:
            # Found!
            return [left, right]
    
    return [-1, -1]
```

## Variations

### Three Sum (Fix + Two Pointers)
```python
def threeSum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for fixed element
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Two pointer search for remaining pair
        left, right = i + 1, len(nums) - 1
        target = -nums[i]
        
        while left < right:
            if nums[left] + nums[right] == target:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
    
    return result
```

### Fast/Slow Pointers (Cycle Detection)
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

---

## Problems

| Problem | Difficulty | Key Insight |
|---------|------------|-------------|
| [3sum.py](file:///c:/Users/amit/Desktop/projects/LeetProject/leetcode/3sum.py) | Medium | Fix + two pointers ✅ |

---

[← Back to Patterns](./README.md)
