# Pattern: Graph (DFS + Backtracking)
# INTUITION:
# Find all paths from node 0 to node n-1 in a DAG.
# DFS with backtracking: add node to path, recurse on neighbors, remove node.
# DAG property means no cycle detection needed.

# Time:  O(p + r * n), p is the count of all the possible paths in graph,
#                      r is the count of the result.
# Space: O(n)

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(graph, curr, path, result):
            if curr == len(graph)-1:
                result.append(path[:])
                return
            for node in graph[curr]:
                path.append(node)
                dfs(graph, node, path, result)
                path.pop()

        result = []
        dfs(graph, 0, [0], result)
        return result

