# Sliding Window Pattern 🪟

## Core Idea
Maintain a window that slides through data, updating state incrementally

## When to Use
- Contiguous subarray/substring problems
- Fixed or variable window size
- Finding longest/shortest subarrays with conditions
- String matching with character counts

## Builds On
- Two Pointers (both use left/right boundaries)

## Template

### Variable Size Window
```python
def sliding_window(s):
    # 1. Initialize window state
    left = 0
    result = 0
    window = {}  # or set, counter, etc.
    
    # 2. Expand window with right pointer
    for right in range(len(s)):
        # 2a. Add right element to window
        char = s[right]
        window[char] = window.get(char, 0) + 1
        
        # 2b. Shrink window while invalid
        while window_is_invalid():
            # Remove left element
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        
        # 2c. Update result with valid window
        result = max(result, right - left + 1)
    
    return result
```

### Fixed Size Window
```python
def fixed_window(nums, k):
    # 1. Build initial window of size k
    window_sum = sum(nums[:k])
    result = window_sum
    
    # 2. Slide window: add right, remove left
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        result = max(result, window_sum)
    
    return result
```

## Key Insight
The `max(left, ...)` trick for position-based windows:

```python
# When duplicate found, jump left past the duplicate
if char in seen:
    left = max(left, seen[char] + 1)
```

Why `max()`? The stored position might be before current left (already outside window).

---

## Problems

| Problem | Difficulty | Key Insight |
|---------|------------|-------------|
| [longest-substring-without-repeating-characters.py](file:///c:/Users/amit/Desktop/projects/LeetProject/leetcode/longest-substring-without-repeating-characters.py) | Medium | HashMap + max() trick ✅ |

---

[← Back to Patterns](./README.md)
