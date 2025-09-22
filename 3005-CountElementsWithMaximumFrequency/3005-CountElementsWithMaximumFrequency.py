# Last updated: 9/22/2025, 3:54:54 PM
class Solution:
  def maxFrequencyElements(self, nums: list[int]) -> int:
    count = collections.Counter(nums)
    maxFreq = max(count.values())
    return sum(freq == maxFreq for freq in count.values()) * maxFreq