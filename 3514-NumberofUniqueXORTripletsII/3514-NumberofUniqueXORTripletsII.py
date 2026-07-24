# Last updated: 7/24/2026, 8:09:48 AM
1class Solution:
2    def uniqueXorTriplets(self, nums: List[int]) -> int:
3        mx = max(nums) << 1
4        st = [False] * mx
5        for a in nums:
6            for b in nums:
7                st[a ^ b] = True
8        s = [0] * mx
9        for ab in range(mx):
10            if st[ab]:
11                for c in nums:
12                    s[ab ^ c] = 1
13        return sum(s)