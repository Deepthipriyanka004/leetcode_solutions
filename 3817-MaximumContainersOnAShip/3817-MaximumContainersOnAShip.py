# Last updated: 6/2/2025, 6:29:27 PM
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        total_cells = n * n  # Total available spaces on the deck
        max_possible_containers = maxWeight // w  # Maximum containers that can be loaded based on weight constraint
        
        return min(total_cells, max_possible_containers)  # Return the minimum of both constraints

# Example test cases
solution = Solution()
print(solution.maxContainers(2, 3, 15))  # Output: 4
print(solution.maxContainers(3, 5, 20))  # Output: 4
