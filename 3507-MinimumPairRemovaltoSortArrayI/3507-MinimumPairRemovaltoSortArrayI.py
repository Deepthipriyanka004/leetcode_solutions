# Last updated: 1/22/2026, 9:19:48 AM
1class Solution:
2  def minimumPairRemoval(self, nums: list[int]) -> int:
3    ans = 0
4
5    while any(x > y for x, y in itertools.pairwise(nums)):
6      pairSums = [x + y for x, y in itertools.pairwise(nums)]
7      minPairSum = min(pairSums)
8      minPairIndex = pairSums.index(minPairSum)
9      nums[minPairIndex] = minPairSum
10      nums.pop(minPairIndex + 1)
11      ans += 1
12
13    return ans