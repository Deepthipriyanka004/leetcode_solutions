# Last updated: 12/5/2025, 4:36:26 PM
1class Solution:
2  def countPartitions(self, nums: list[int]) -> int:
3    # If we add the same number in the left subarray and remove it from the
4    # right subarray, then the difference remains the same parity. So, just
5    # return the number of ways to partition the array into two subarrays when
6    # the array sum is even.
7    return len(nums) - 1 if sum(nums) % 2 == 0 else 0
8