# Last updated: 12/9/2025, 8:05:55 PM
1class Solution:
2    def specialTriplets(self, nums: List[int]) -> int:
3        dict1 = {}
4        dict2 = {}
5        res = 0
6        mod = 10 ** 9 + 7   # Fixed exponentiation operator
7        
8        for num in nums:
9            if num % 2 == 0 and num // 2 in dict2:
10                res += dict2[num // 2]
11                res %= mod  # Fixed: previously was `res = mod`
12            
13            if num * 2 in dict1:
14                if num in dict2:
15                    dict2[num] += dict1[num * 2]
16                else:
17                    dict2[num] = dict1[num * 2]
18            
19            if num in dict1:
20                dict1[num] += 1
21            else:
22                dict1[num] = 1
23        
24        return res % mod
25