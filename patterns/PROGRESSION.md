# 🎯 Pattern Learning Progression

> **How to use**: Follow this roadmap sequentially. Each tier builds on concepts from the previous tier.

---

## Tier 1: Foundations (Start Here)
*Master these first - they appear in 60%+ of problems*

```
┌─────────────────────────────────────────────────────────────────┐
│  [Arrays/Strings] ──► [Hash Map] ──► [Two Pointers] ──► [Binary Search]  │
│       ▼                                                         │
│  Basic iteration     O(1) lookup    O(n) to O(n²)    O(log n)   │
└─────────────────────────────────────────────────────────────────┘
```

| Pattern | Prerequisite | Key Insight | Problems to Master |
|---------|--------------|-------------|-------------------|
| **Hash Map** | Arrays | Trade space for O(1) lookup | Two Sum, Group Anagrams |
| **Two Pointers** | Sorting | Move inward/outward based on condition | 3Sum, Container With Water |
| **Binary Search** | Sorted arrays | Eliminate half each iteration | Search Insert, Peak Element |

---

## Tier 2: Linear Structures
*Build on Tier 1 concepts*

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│  [Two Pointers] ──► [Sliding Window]    [Arrays] ──► [Stack]    │
│                           │                              │       │
│                           ▼                              ▼       │
│                    [Linked List] ◄──────────── [Monotonic Stack] │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Pattern | Builds On | Key Insight | Problems to Master |
|---------|-----------|-------------|-------------------|
| **Sliding Window** | Two Pointers | Expand right, shrink left | Min Window Substring, Longest Substring |
| **Stack** | Arrays | LIFO for matching/nesting | Valid Parentheses, Daily Temperatures |
| **Monotonic Stack** | Stack | Maintain order for next greater/smaller | NGE, Largest Rectangle |
| **Linked List** | Pointers | Dummy nodes, fast/slow | Reverse, Merge, Cycle Detection |

---

## Tier 3: Recursion & Trees
*Requires comfort with recursion*

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│  [Recursion] ──► [Binary Tree DFS] ──► [BST Operations]         │
│       │                │                                         │
│       ▼                ▼                                         │
│  [Backtracking]   [Tree BFS]                                     │
│       │                                                          │
│       ▼                                                          │
│  [Subsets/Permutations/Combinations]                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Pattern | Builds On | Key Insight | Problems to Master |
|---------|-----------|-------------|-------------------|
| **Tree DFS** | Recursion | Pre/In/Post order traversal | Max Depth, Path Sum |
| **Tree BFS** | Queue | Level-order processing | Level Order, Right Side View |
| **Backtracking** | Recursion | Choose → Explore → Unchoose | Permutations, N-Queens, Subsets |

---

## Tier 4: Graph Patterns
*Extends tree concepts to general graphs*

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│  [Tree DFS/BFS] ──► [Graph DFS] ──► [Topological Sort]          │
│                          │                                       │
│                          ▼                                       │
│                    [Graph BFS] ──► [Shortest Path]               │
│                          │                                       │
│                          ▼                                       │
│                    [Union-Find] ──► [MST (Kruskal)]              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Pattern | Builds On | Key Insight | Problems to Master |
|---------|-----------|-------------|-------------------|
| **Graph DFS** | Tree DFS + visited set | Cycle detection, path finding | Number of Islands, Clone Graph |
| **Graph BFS** | Tree BFS + visited set | Shortest path (unweighted) | Word Ladder, Rotting Oranges |
| **Topological Sort** | Graph DFS | Dependencies, ordering | Course Schedule |
| **Union-Find** | Arrays | Dynamic connectivity | Accounts Merge, Redundant Connection |

---

## Tier 5: Dynamic Programming
*Requires mastering recursion first*

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│  [Recursion] ──► [Memoization] ──► [1D DP] ──► [2D DP]          │
│                                         │          │             │
│                                         ▼          ▼             │
│                                   [Kadane's]  [Grid DP]          │
│                                                    │             │
│                                                    ▼             │
│                                            [Interval DP]         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Pattern | Builds On | Key Insight | Problems to Master |
|---------|-----------|-------------|-------------------|
| **1D DP** | Memoization | dp[i] depends on previous states | Climbing Stairs, House Robber |
| **2D DP** | 1D DP | Two dimensions of state | Edit Distance, LCS |
| **Grid DP** | 2D DP | Path/count in matrix | Unique Paths, Min Path Sum |
| **Interval DP** | 2D DP | Process ranges | Burst Balloons, Palindrome Partition |

---

## Tier 6: Advanced Patterns
*For competitive programming and hard problems*

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│  [Hash Map] ──► [Trie] ──► [Suffix Array/Tree]                  │
│                                                                  │
│  [Binary Search] ──► [Segment Tree] ──► [BIT/Fenwick]           │
│                                                                  │
│  [Math] ──► [Bit Manipulation] ──► [Bitmask DP]                 │
│                                                                  │
│  [Greedy] ──► [Dijkstra] ──► [A* Search]                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Pattern | Builds On | Key Insight | Problems to Master |
|---------|-----------|-------------|-------------------|
| **Trie** | Hash Map | Prefix tree for strings | Implement Trie, Word Search II |
| **Greedy** | Sorting | Local optimum → global | Jump Game, Gas Station |
| **Bit Manipulation** | Math | XOR tricks, bitmasks | Single Number, Counting Bits |
| **Heap** | Arrays | Priority queue for top-k | Merge K Lists, Find Median |

---

## Pattern Discovery Flow

When analyzing a new problem:

```
1. Read problem → Identify constraints
          ↓
2. Check if it matches known patterns:
   • Sorted array? → Binary Search / Two Pointers
   • Substrings/subarrays? → Sliding Window
   • All combinations? → Backtracking
   • Optimal substructure? → DP
   • Graph/connectivity? → DFS/BFS/Union-Find
          ↓
3. If new pattern found → Create/update pattern guide
          ↓
4. Add problem to pattern's "Key Problems" list
```

---

## Progress Tracking

| Tier | Patterns | Mastered |
|------|----------|----------|
| 1 | Hash Map, Two Pointers, Binary Search | ⬜⬜⬜ |
| 2 | Sliding Window, Stack, Monotonic Stack, Linked List | ⬜⬜⬜⬜ |
| 3 | Tree DFS, Tree BFS, Backtracking | ⬜⬜⬜ |
| 4 | Graph DFS, Graph BFS, Topological Sort, Union-Find | ⬜⬜⬜⬜ |
| 5 | 1D DP, 2D DP, Grid DP, Interval DP | ⬜⬜⬜⬜ |
| 6 | Trie, Greedy, Bit Manipulation, Heap | ⬜⬜⬜⬜ |

*Mark ✅ as you complete 5+ problems in each pattern*
