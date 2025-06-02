# Last updated: 6/2/2025, 6:29:20 PM
from typing import List

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        answer = [float('inf')] * n
        
        # Maintain the minimum cost seen so far
        min_cost = float('inf')
        
        for i in range(n):
            min_cost = min(min_cost, cost[i])
            answer[i] = min_cost
        
        return answer

# Example test cases
sol = Solution()
print(sol.minCosts([5,3,4,1,3,2]))  # Output: [5,3,3,1,1,1]
print(sol.minCosts([1,2,4,6,7]))    # Output: [1,1,1,1,1]