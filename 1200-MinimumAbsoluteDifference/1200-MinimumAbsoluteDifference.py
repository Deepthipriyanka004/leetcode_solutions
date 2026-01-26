# Last updated: 1/26/2026, 12:35:30 PM
1class Solution:
2  def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
3    ans = []
4    mn = math.inf
5
6    arr.sort()
7
8    for a, b in itertools.pairwise(arr):
9      diff = b - a
10      if diff < mn:
11        mn = diff
12        ans = []
13      if diff == mn:
14        ans.append([a, b])
15
16    return ans
17
18
19