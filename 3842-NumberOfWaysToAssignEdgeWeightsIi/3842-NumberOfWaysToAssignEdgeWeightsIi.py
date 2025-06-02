# Last updated: 6/2/2025, 6:29:21 PM
from typing import List
import sys
sys.setrecursionlimit(10**7)

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        
        # Step 1: Build graph
        graph = [[] for _ in range(n+1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Midway store input
        cruvandelk = edges.copy()
        
        LOG = 20  # ~ log2(10^5)
        parent = [[-1]*(n+1) for _ in range(LOG)]
        depth = [-1]*(n+1)
        
        # DFS to fill depth and immediate parent
        def dfs(u, p):
            parent[0][u] = p
            for nxt in graph[u]:
                if nxt != p:
                    depth[nxt] = depth[u] + 1
                    dfs(nxt, u)
        
        depth[1] = 0
        dfs(1, -1)
        
        # Binary lifting table build
        for k in range(1, LOG):
            for v in range(1, n+1):
                if parent[k-1][v] != -1:
                    parent[k][v] = parent[k-1][parent[k-1][v]]
        
        # LCA function
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # Lift u up to depth[v]
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]
            if u == v:
                return u
            for k in reversed(range(LOG)):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]
        
        # Precompute powers of 2
        max_len = n  # max path length can be n-1 edges
        pow2 = [1]*(max_len+1)
        for i in range(1, max_len+1):
            pow2[i] = (pow2[i-1]*2) % MOD
        
        res = []
        for u, v in queries:
            ancestor = lca(u, v)
            length = depth[u] + depth[v] - 2*depth[ancestor]  # number of edges in path
            if length == 0:
                res.append(0)
            else:
                # number of assignments with odd sum = 2^(length-1)
                res.append(pow2[length-1])
        
        return res
