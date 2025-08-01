# Last updated: 6/2/2025, 6:36:48 PM
class Solution:
  def numRabbits(self, answers: list[int]) -> int:
    ans = 0
    count = collections.Counter()

    for answer in answers:
      if count[answer] % (answer + 1) == 0:
        ans += answer + 1
      count[answer] += 1

    return ans