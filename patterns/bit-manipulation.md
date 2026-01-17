# Bit Manipulation Pattern

## Core Concept
Use binary operations for efficient computation. Key operations: AND, OR, XOR, NOT, shifts.

---

## Essential Operations

```python
# Check if bit is set
(n >> i) & 1

# Set bit
n | (1 << i)

# Clear bit
n & ~(1 << i)

# Toggle bit
n ^ (1 << i)

# Count set bits
bin(n).count('1')  # or n.bit_count() in Python 3.10+

# Check power of 2
n > 0 and (n & (n - 1)) == 0

# Get lowest set bit
n & (-n)

# Clear lowest set bit
n & (n - 1)
```

---

## Key Tricks

| Trick | Code | Use Case |
|-------|------|----------|
| XOR cancellation | `a ^ a = 0` | Find unique element |
| XOR identity | `a ^ 0 = a` | Preserve value |
| Swap without temp | `a ^= b; b ^= a; a ^= b` | In-place swap |
| Check odd/even | `n & 1` | Faster than `n % 2` |

---

## Key Problems

| Problem | Pattern |
|---------|---------|
| [Single Number](../solutions/single-number.py) | XOR all elements |
| [Missing Number](../solutions/missing-number.py) | XOR with indices |
| [Power of Two](../solutions/power-of-two.py) | n & (n-1) == 0 |
| [Counting Bits](../solutions/counting-bits.py) | DP with bit trick |
| [Reverse Bits](../solutions/reverse-bits.py) | Bit-by-bit reversal |
| [Number of 1 Bits](../solutions/number-of-1-bits.py) | Brian Kernighan's |

---

## Complexity
- **Time:** O(1) for fixed-width integers, O(log n) for arbitrary
- **Space:** O(1)
