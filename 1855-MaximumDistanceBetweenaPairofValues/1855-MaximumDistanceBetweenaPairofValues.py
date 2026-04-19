# Last updated: 4/19/2026, 9:56:48 AM
1class Solution:
2  def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
3    ans = 0
4    i = 0
5    j = 0
6
7    while i < len(nums1) and j < len(nums2):
8      if nums1[i] > nums2[j]:
9        i += 1
10      else:
11        ans = max(ans, j - i)
12        j += 1
13
14    return ans
15
16