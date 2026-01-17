# Monotonic Stack Pattern

## Core Concept
A stack that maintains elements in strictly increasing or decreasing order. Used to find the **next/previous greater/smaller element** efficiently.

---

## Template

```python
def monotonic_stack(nums):
    stack = []  # stores indices
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        # For next greater element (decreasing stack)
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result
```

---

## When to Use
- **Next Greater Element** - Find first larger element to the right
- **Previous Greater Element** - Find first larger element to the left
- **Histogram problems** - Largest rectangle, trapping rain water
- **132 Pattern** - Find specific ordering in array

---

## Key Problems

| Problem | Variant |
|---------|---------|
| [Next Greater Element I](../solutions/next-greater-element-i.py) | Basic NGE |
| [Next Greater Element II](../solutions/next-greater-element-ii.py) | Circular array |
| [Daily Temperatures](../solutions/daily-temperatures.py) | Days until warmer |
| [132 Pattern](../solutions/132-pattern.py) | Decreasing stack |
| [Largest Rectangle in Histogram](../solutions/largest-rectangle-in-histogram.py) | Area calculation |
| [Trapping Rain Water](../solutions/trapping-rain-water.py) | Two-pass or stack |

---

## Complexity
- **Time:** O(n) - each element pushed and popped at most once
- **Space:** O(n) - stack storage
