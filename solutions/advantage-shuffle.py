# Pattern: Greedy (Sorting + Matching)
# INTUITION:
# Maximize advantage: for each B[i], use smallest A[j] that beats it.
# Sort both arrays. Greedily match A elements to B elements.
# If A[j] can't beat current B, save it for later (others array).

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sortedA = sorted(A)
        sortedB = sorted(B)

        candidates = {b: [] for b in B}
        others = []
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                candidates[sortedB[j]].append(a)
                j += 1
            else:
                others.append(a)
        return [candidates[b].pop() if candidates[b] else others.pop()
                for b in B]

