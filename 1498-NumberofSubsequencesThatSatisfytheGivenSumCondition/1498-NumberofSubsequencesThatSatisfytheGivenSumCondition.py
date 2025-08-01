# Last updated: 6/29/2025, 12:55:29 PM
class Solution:
  def numSubseq(self, nums: list[int], target: int) -> int:
    MOD = 1_000_000_007
    n = len(nums)
    ans = 0

    nums.sort()

    l = 0
    r = n - 1
    while l <= r:
      if nums[l] + nums[r] <= target:
        ans += pow(2, r - l, MOD)
        l += 1
      else:
        r -= 1

    return ans % MOD