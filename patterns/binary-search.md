# Binary Search Pattern 🔍

## Core Idea
Eliminate half the search space each iteration → O(log n)

## When to Use
- Sorted array/range
- Finding boundary conditions (first/last occurrence)
- Optimization problems (min/max that satisfies condition)
- Search in rotated/modified sorted arrays

## Template

```python
def binary_search(nums, target):
    # 1. Define search boundaries (inclusive)
    left, right = 0, len(nums) - 1
    
    # 2. Search while range is valid
    while left <= right:
        # 2a. Calculate mid (overflow-safe)
        mid = left + (right - left) // 2
        
        # 2b. Compare and narrow search space
        if nums[mid] > target:
            right = mid - 1  # Target in left half
        elif nums[mid] < target:
            left = mid + 1   # Target in right half
        else:
            return mid       # Found!
    
    # 3. Not found
    return -1
```

## Variations

### Find First Occurrence
```python
while left < right:
    mid = left + (right - left) // 2
    if nums[mid] >= target:
        right = mid      # Keep searching left
    else:
        left = mid + 1
return left if nums[left] == target else -1
```

### Find Last Occurrence
```python
while left < right:
    mid = left + (right - left + 1) // 2  # Bias right
    if nums[mid] <= target:
        left = mid       # Keep searching right
    else:
        right = mid - 1
return left if nums[left] == target else -1
```

---

## Problems

| Problem | Difficulty | Key Insight |
|---------|------------|-------------|
| [binary-search.py](file:///c:/Users/amit/Desktop/projects/LeetProject/leetcode/binary-search.py) | Easy | Classic template ✅ |

---

[← Back to Patterns](./README.md)
