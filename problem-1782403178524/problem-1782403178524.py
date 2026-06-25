# Last updated: 6/25/2026, 9:29:38 PM
1class Solution:
2    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
3        n = len(nums)
4        ans = 0
5        for i in range(n):
6            cnt = 0
7            for j in range(i, n):
8                cnt += int(nums[j] == target)
9                if cnt * 2 > j - i + 1:
10                    ans += 1
11        return ans