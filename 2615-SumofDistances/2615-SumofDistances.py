# Last updated: 4/24/2026, 8:04:45 PM
1class Solution:
2  def distance(self, nums: list[int]) -> list[int]:
3    ans = [0] * len(nums)
4    numToIndices = collections.defaultdict(list)
5
6    for i, num in enumerate(nums):
7      numToIndices[num].append(i)
8
9    for indices in numToIndices.values():
10      n = len(indices)
11      if n == 1:
12        continue
13      sumSoFar = sum(indices)
14      prevIndex = 0
15      for i in range(n):
16        sumSoFar += (i - 1) * (indices[i] - prevIndex)
17        sumSoFar -= (n - 1 - i) * (indices[i] - prevIndex)
18        ans[indices[i]] = sumSoFar
19        prevIndex = indices[i]
20
21    return ans