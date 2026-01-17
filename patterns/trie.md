# Trie (Prefix Tree) Pattern

## Core Concept
A tree structure for storing strings where each node represents a character. Enables **O(m) prefix lookups** where m = word length.

---

## Template

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_end
    
    def startsWith(self, prefix):
        return self._find(prefix) is not None
    
    def _find(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
```

---

## When to Use
- **Autocomplete** - Find all words with prefix
- **Spell Checker** - Word existence check
- **Word Search II** - Multiple patterns in grid
- **Wildcard Matching** - Search with '.' wildcard
- **Prefix Matching** - Count/find words by prefix

---

## Key Problems

| Problem | Variant |
|---------|---------|
| [Implement Trie](../solutions/implement-trie-prefix-tree.py) | Basic implementation |
| [Add and Search Word](../solutions/add-and-search-word-data-structure-design.py) | Wildcard '.' support |
| [Word Search II](../solutions/word-search.py) | Grid + multiple words |
| [Longest Word in Dictionary](../solutions/longest-word-in-dictionary.py) | Build from prefixes |

---

## Complexity
- **Insert/Search:** O(m) where m = word length
- **Space:** O(n * m) worst case for n words
