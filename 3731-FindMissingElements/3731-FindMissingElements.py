# Last updated: 8/4/2026, 10:56:53 PM
1class Solution:
2    def findMissingElements(self, nums: List[int]) -> List[int]:
3        mn, mx = min(nums), max(nums)
4        s = set(nums)
5        return [x for x in range(mn + 1, mx) if x not in s]