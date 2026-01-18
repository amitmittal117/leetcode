# Pattern: Hash Map + Combinatorics
# INTUITION:
# Group visits by user, sort by time. Generate all 3-website combinations per user.
# Count unique patterns across users. Return lexicographically smallest with max count.

# Time:  O(n^3)
# Space: O(n^3)

import collections
import itertools


class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        lookup = collections.defaultdict(list)
        A = zip(timestamp, username, website)
        A.sort()
        for t, u, w in A:
            lookup[u].append(w)
        count = sum([collections.Counter(set(itertools.combinations(lookup[u], 3))) for u in lookup], collections.Counter())
        return list(min(count, key=lambda x: (-count[x], x)))
