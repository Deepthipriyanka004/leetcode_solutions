# Last updated: 10/4/2025, 9:19:53 PM
class Solution:
  def maxArea(self, height: list[int]) -> int:
    ans = 0
    l = 0
    r = len(height) - 1

    while l < r:
      minHeight = min(height[l], height[r])
      ans = max(ans, minHeight * (r - l))
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1

    return ans