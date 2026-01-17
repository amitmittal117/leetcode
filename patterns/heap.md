# Heap / Priority Queue Pattern

## Core Concept
Maintain **quick access to min/max element** while supporting dynamic insertions. Python's `heapq` is a min-heap by default.

---

## Template

```python
import heapq

# Min Heap (default)
heap = []
heapq.heappush(heap, value)
min_val = heapq.heappop(heap)
peek = heap[0]

# Max Heap (negate values)
heapq.heappush(heap, -value)
max_val = -heapq.heappop(heap)

# Heapify existing list
heapq.heapify(nums)  # O(n)

# K largest/smallest
largest_k = heapq.nlargest(k, nums)
smallest_k = heapq.nsmallest(k, nums)
```

---

## When to Use
- **Kth Largest/Smallest** - Maintain k-sized heap
- **Merge K Sorted Lists** - Pop smallest, push next
- **Top K Frequent** - Heap of (freq, element)
- **Median Finder** - Two heaps (max-heap + min-heap)
- **Meeting Rooms II** - Track end times

---

## Key Problems

| Problem | Variant |
|---------|---------|
| [Kth Largest Element](../solutions/kth-largest-element-in-an-array.py) | Min-heap of size k |
| [Merge K Sorted Lists](../solutions/merge-k-sorted-lists.py) | Multi-way merge |
| [Top K Frequent Elements](../solutions/top-k-frequent-elements.py) | Frequency counting |
| [Find Median from Stream](../solutions/find-median-from-data-stream.py) | Two heaps |
| [Task Scheduler](../solutions/meeting-rooms-ii.py) | End time tracking |

---

## Complexity
- **Push/Pop:** O(log n)
- **Peek:** O(1)
- **Heapify:** O(n)
- **Space:** O(n) or O(k) for k-sized heap
