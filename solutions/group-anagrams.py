# Time:  O(n * glogg), g is the max size of groups.
# Space: O(n)
# Pattern: Hash Map (Grouping)
#
# INTUITION:
# Anagrams have same letters, just rearranged. Sorting a string gives canonical
# form: all anagrams sort to same string. Use sorted string as hashmap key,
# group original strings together. O(n × k log k) where k = max string length.

import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 1. Map: sorted string -> list of original strings
        anagrams_map, result = collections.defaultdict(list), []
        
        # 2. Group by sorted representation
        for s in strs:
            sorted_str = ("").join(sorted(s))
            anagrams_map[sorted_str].append(s)
        
        # 3. Collect results
        for anagram in anagrams_map.values():
            anagram.sort()
            result.append(anagram)
        return result
