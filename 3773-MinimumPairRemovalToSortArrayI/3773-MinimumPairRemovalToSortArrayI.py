# Last updated: 6/2/2025, 6:29:43 PM
from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True
        
        # Count operations
        operations = 0
        
        # Continue the process until the array is non-decreasing
        while not is_non_decreasing(nums):
            # Find the adjacent pair with the minimum sum
            min_sum = float('inf')
            min_index = -1
            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_index = i
            
            # Merge the selected pair
            nums[min_index] = nums[min_index] + nums[min_index + 1]
            nums.pop(min_index + 1)
            
            # Increase the operation count
            operations += 1
        
        return operations
