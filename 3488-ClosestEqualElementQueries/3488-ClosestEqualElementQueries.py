# Last updated: 4/16/2026, 9:28:29 AM
1class Solution:
2  def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
3    n = len(nums)
4    # minDist[i] := the minimum distance between nums[i], and any other index j
5    # in the circular array, where nums[j] == nums[i]
6    minDist = [n] * n
7    lastSeen = {}
8
9    for i in range(n * 2):
10      index = i % n
11      num = nums[index]
12      if num in lastSeen:
13        prevIndex = lastSeen[num] % n
14        d = i - prevIndex
15        minDist[index] = min(minDist[index], d)
16        minDist[prevIndex] = min(minDist[prevIndex], d)
17      lastSeen[num] = i
18
19    return [-1 if minDist[query] == n
20            else minDist[query]
21            for query in queries]