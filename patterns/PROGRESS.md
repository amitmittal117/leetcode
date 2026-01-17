# LeetCode Enhancement Progress Tracker

> **Resume command:** "Resume from progress tracker"

---

## Auto-Detection

Files with `# Pattern:` tag = processed.
```bash
findstr /M "# Pattern:" *.py    # Windows
```

**Current count: 23 / 3056 files processed**

---

## Git Workflow

After each batch:
1. `git add .` - stage all changes
2. `git commit -m "Add structured comments to [X] files (batch N)"` - commit
3. **User reviews** - then `git push` when ready

---

## Custom Mind Maps

For company-specific or topic-specific question sets:

**To create/add to a mind map:**
> "Create mind map: [Name]" + list of questions  
> "Add to [Name] mind map" + more questions

**Location:** `patterns/mindmaps/[name].md`

**Available:** See [mindmaps/README.md](./mindmaps/README.md)



---

## Completed Files ✅

| File | Pattern |
|------|---------|
| binary-search.py | Binary Search |
| search-in-rotated-sorted-array.py | Binary Search |
| 3sum.py | Two Pointers |
| container-with-most-water.py | Two Pointers |
| trapping-rain-water.py | Two Pointers |
| longest-substring-without-repeating-characters.py | Sliding Window |
| minimum-window-substring.py | Sliding Window |
| add-two-numbers.py | Linked List |
| reverse-linked-list.py | Linked List |
| merge-two-sorted-lists.py | Linked List |
| linked-list-cycle.py | Linked List |
| valid-parentheses.py | Stack |
| daily-temperatures.py | Stack (Monotonic) |
| number-of-islands.py | Graph/DFS |
| course-schedule.py | Graph (Topological Sort) |
| climbing-stairs.py | DP |
| coin-change.py | DP |
| house-robber.py | DP |
| longest-increasing-subsequence.py | DP + Binary Search |
| word-break.py | DP |
| permutations.py | Backtracking |
| subsets.py | Backtracking |
| combination-sum.py | Backtracking |

---

## Patterns Covered (9 total)

| Pattern | Count |
|---------|-------|
| Binary Search | 2 |
| Two Pointers | 3 |
| Sliding Window | 2 |
| Linked List | 4 |
| Stack | 2 |
| Graph | 2 |
| DP | 5 |
| Backtracking | 3 |

---

## Batch Processing

- **Batch 1 (10):** ✅ Complete
- **Batch 2 (10):** 8/10 done (next: 2 more, then batch 3 of 16 per Fibonacci)

## Next in Queue

- [ ] edit-distance.py (DP)
- [ ] jump-game.py (Greedy) 
- [ ] best-time-to-buy-and-sell-stock.py (DP/Greedy)
