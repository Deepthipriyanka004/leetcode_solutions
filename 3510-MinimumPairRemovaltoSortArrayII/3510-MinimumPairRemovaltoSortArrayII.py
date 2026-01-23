# Last updated: 1/23/2026, 11:04:44 AM
1from sortedcontainers import SortedList
2
3
4class Solution:
5  def minimumPairRemoval(self, nums: list[int]) -> int:
6    n = len(nums)
7    ans = 0
8    inversionsCount = sum(nums[i + 1] < nums[i] for i in range(n - 1))
9    nextIndices = [i + 1 for i in range(n)]
10    prevIndices = [i - 1 for i in range(n)]
11    pairSums = SortedList((a + b, i)
12                          for i, (a, b) in enumerate(itertools.pairwise(nums)))
13
14    while inversionsCount > 0:
15      ans += 1
16      smallestPair = pairSums.pop(0)
17      pairSum, currIndex = smallestPair
18      nextIndex = nextIndices[currIndex]
19      prevIndex = prevIndices[currIndex]
20
21      if prevIndex >= 0:
22        oldPairSum = nums[prevIndex] + nums[currIndex]
23        newPairSum = nums[prevIndex] + pairSum
24        pairSums.remove((oldPairSum, prevIndex))
25        pairSums.add((newPairSum, prevIndex))
26        if nums[prevIndex] > nums[currIndex]:
27          inversionsCount -= 1
28        if nums[prevIndex] > pairSum:
29          inversionsCount += 1
30
31      if nums[nextIndex] < nums[currIndex]:
32        inversionsCount -= 1
33
34      nextNextIndex = nextIndices[nextIndex] if nextIndex < n else n
35      if nextNextIndex < n:
36        oldPairSum = nums[nextIndex] + nums[nextNextIndex]
37        newPairSum = pairSum + nums[nextNextIndex]
38        pairSums.remove((oldPairSum, nextIndex))
39        pairSums.add((newPairSum, currIndex))
40        if nums[nextNextIndex] < nums[nextIndex]:
41          inversionsCount -= 1
42        if nums[nextNextIndex] < pairSum:
43          inversionsCount += 1
44        prevIndices[nextNextIndex] = currIndex
45
46      nextIndices[currIndex] = nextNextIndex
47      nums[currIndex] = pairSum
48
49    return ans