# Last updated: 7/19/2025, 10:16:35 AM
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n= len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return[]
obj=Solution()
print(obj.twoSum([2,7,11,15],9))            