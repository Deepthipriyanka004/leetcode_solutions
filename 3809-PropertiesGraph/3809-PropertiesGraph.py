# Last updated: 6/2/2025, 6:29:37 PM
from typing import List
from collections import defaultdict

class Solution:
    def intersect(self, a: List[int], b: List[int]) -> int:
        return len(set(a) & set(b))
    
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        graph = defaultdict(list)
        
        # Build the graph
        for i in range(n):
            for j in range(i + 1, n):
                if self.intersect(properties[i], properties[j]) >= k:
                    graph[i].append(j)
                    graph[j].append(i)
        
        # Perform BFS/DFS to count connected components
        visited = set()
        def dfs(node):
            stack = [node]
            while stack:
                curr = stack.pop()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
        
        components = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                components += 1
        
        return components

# Example test cases
solution = Solution()
print(solution.numberOfComponents([[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], 1))  # Output: 3
print(solution.numberOfComponents([[1,2,3],[2,3,4],[4,3,5]], 2))  # Output: 1
print(solution.numberOfComponents([[1,1],[1,1]], 2))  # Output: 2