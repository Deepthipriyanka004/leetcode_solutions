# Last updated: 3/7/2026, 9:22:48 AM
1class Solution:
2  def minFlips(self, s: str) -> int:
3    n = len(s)
4    # count[0][0] :=  the number of '0' in the even indices
5    # count[0][1] :=  the number of '0' in the odd indices
6    # count[1][0] :=  the number of '1' in the even indices
7    # count[1][1] :=  the number of '1' in the odd indices
8    count = [[0] * 2 for _ in range(2)]
9
10    for i, c in enumerate(s):
11      count[int(c)][i % 2] += 1
12
13    # min(make all 0s in the even indices + make all 1s in the odd indices,
14    #     make all 1s in the even indices + make all 0s in the odd indices)
15    ans = min(count[1][0] + count[0][1], count[0][0] + count[1][1])
16
17    for i, c in enumerate(s):
18      count[int(c)][i % 2] -= 1
19      count[int(c)][(n + i) % 2] += 1
20      ans = min(ans, count[1][0] + count[0][1], count[0][0] + count[1][1])
21
22    return ans