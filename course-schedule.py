# course-schedule.py
# Time:  O(|V| + |E|)
# Space: O(|E|)
# Pattern: Graph (Topological Sort / Kahn's Algorithm)

import collections


# Khan's algorithm (bfs solution)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Key insight: Course schedule is possible iff no cycle in dependency graph
        # Use topological sort - process nodes with no incoming edges first
        
        # 1. Build adjacency list and count in-degrees
        #    - in_degree[u] = number of prerequisites for course u
        adj = collections.defaultdict(list)
        in_degree = collections.Counter()
        for u, v in prerequisites:
            in_degree[u] += 1      # u depends on v
            adj[v].append(u)       # v -> u (v must come before u)
        
        # 2. Start with courses that have no prerequisites
        result = []
        q = [u for u in xrange(numCourses) if u not in in_degree]
        
        # 3. BFS: process each course and unlock dependents
        while q:
            new_q = []
            for u in q:
                result.append(u)
                # 3a. For each course that depends on u
                for v in adj[u]:
                    # 3b. Remove this dependency
                    in_degree[v] -= 1
                    # 3c. If no more prerequisites, add to queue
                    if in_degree[v] == 0:
                        new_q.append(v)
            q = new_q
        
        # 4. If we processed all courses, schedule is possible
        #    Otherwise, there's a cycle (unprocessed courses remain)
        return len(result) == numCourses


# Time:  O(|V| + |E|)
# Space: O(|E|)
import collections


# dfs solution
class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = collections.defaultdict(list)
        in_degree = collections.Counter()
        for u, v in prerequisites:
            in_degree[u] += 1
            adj[v].append(u)
        result = []
        stk = [u for u in xrange(numCourses) if u not in in_degree]
        while stk:
            u = stk.pop()
            result.append(u)
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    stk.append(v)
        return len(result) == numCourses
