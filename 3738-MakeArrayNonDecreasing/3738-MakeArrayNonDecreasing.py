# Last updated: 6/2/2025, 6:29:44 PM
from typing import List

class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []
        
        for num in nums:
            # When stack is non-empty and top is greater than current number,
            # we have to merge to maintain non-decreasing order.
            while stack and stack[-1] > num:
                top = stack.pop()
                # We merge: current number becomes max of the merged subarray
                num = max(num, top)
            stack.append(num)
        
        return len(stack)
