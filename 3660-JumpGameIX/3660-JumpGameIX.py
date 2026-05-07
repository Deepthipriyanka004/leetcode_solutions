# Last updated: 5/7/2026, 9:47:41 PM
1class Solution:
2    def maxValue(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        ans = [0] * n
5        pre_max = [nums[0]] * n
6        for i in range(1, n):
7            pre_max[i] = max(pre_max[i - 1], nums[i])
8        suf_min = inf
9        for i in range(n - 1, -1, -1):
10            ans[i] = ans[i + 1] if pre_max[i] > suf_min else pre_max[i]
11            suf_min = min(suf_min, nums[i])
12        return ans