# Last updated: 11/27/2025, 3:40:43 PM
1class Solution:
2  def maxSubarraySum(self, nums: list[int], k: int) -> int:
3    ans = -math.inf
4    prefix = 0
5    # minPrefix[i % k] := the minimum prefix sum of the first i numbers
6    minPrefix = [math.inf] * k
7    minPrefix[k - 1] = 0
8
9    for i, num in enumerate(nums):
10      prefix += num
11      ans = max(ans, prefix - minPrefix[i % k])
12      minPrefix[i % k] = min(minPrefix[i % k], prefix)
13
14    return ans