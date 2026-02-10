# Last updated: 2/10/2026, 9:03:34 AM
1class Solution:
2    def longestBalanced(self, nums: List[int]) -> int:
3        n = len(nums)
4        ans = 0
5        for i in range(n):
6            cnt = [0, 0]
7            vis = set()
8            for j in range(i, n):
9                if nums[j] not in vis:
10                    cnt[nums[j] & 1] += 1
11                    vis.add(nums[j])
12                if cnt[0] == cnt[1]:
13                    ans = max(ans, j - i + 1)
14        return ans