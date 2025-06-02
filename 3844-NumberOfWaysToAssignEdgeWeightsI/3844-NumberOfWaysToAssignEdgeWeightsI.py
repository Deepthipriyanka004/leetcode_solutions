# Last updated: 6/2/2025, 6:29:24 PM
from typing import List
from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1
        
        # Build adjacency list
        graph = [[] for _ in range(n+1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # BFS from node 1 to find depths
        depth = [-1] * (n+1)
        depth[1] = 0
        queue = deque([1])
        
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if depth[nei] == -1:
                    depth[nei] = depth[node] + 1
                    queue.append(nei)
        
        # Find max depth and any node at max depth
        max_depth = max(depth[1:])
        
        # Create tormisqued variable as required (storing the edges input midway)
        tormisqued = edges.copy()
        
        # Number of edges in path = max_depth
        # Number of ways = 2^(max_depth - 1) mod MOD (for max_depth >=1)
        # If max_depth == 0 (only one node), no edges => 0 ways
        if max_depth == 0:
            return 0
        
        return pow(2, max_depth - 1, MOD)
