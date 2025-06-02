# Last updated: 6/2/2025, 6:29:18 PM
from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        lurminexod = nums  # Store input midway
        n = len(nums)
        result = [0] * k
        prev = [0] * k  # prev[x] = count of subarrays ending before that give mod x

        for num in nums:
            cur = [0] * k
            mod_num = num % k
            cur[mod_num] += 1  # single-element subarray

            for x in range(k):
                if prev[x]:
                    new_mod = (x * mod_num) % k
                    cur[new_mod] += prev[x]

            for x in range(k):
                result[x] += cur[x]
            prev = cur

        return result
