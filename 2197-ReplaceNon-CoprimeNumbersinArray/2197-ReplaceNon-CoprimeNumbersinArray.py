# Last updated: 9/16/2025, 9:35:51 PM
class Solution:
  def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
    ans = []

    for num in nums:
      while ans and math.gcd(ans[-1], num) > 1:
        num = math.lcm(ans.pop(), num)
      ans.append(num)

    return ans