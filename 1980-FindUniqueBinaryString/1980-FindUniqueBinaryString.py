# Last updated: 3/8/2026, 10:10:30 AM
1class Solution:
2  def findDifferentBinaryString(self, nums: list[str]) -> str:
3    bitSize = len(nums[0])
4    maxNum = 1 << bitSize
5    numsSet = {int(num, 2) for num in nums}
6
7    for num in range(maxNum):
8      if num not in numsSet:
9        return f'{num:0>{bitSize}b}'