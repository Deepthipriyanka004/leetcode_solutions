# Last updated: 6/2/2025, 6:33:19 PM
class Solution:
  def longestPalindrome(self, words: list[str]) -> int:
    ans = 0
    count = [[0] * 26 for _ in range(26)]

    for a, b in words:
      i = ord(a) - ord('a')
      j = ord(b) - ord('a')
      if count[j][i]:
        ans += 4
        count[j][i] -= 1
      else:
        count[i][j] += 1

    for i in range(26):
      if count[i][i]:
        return ans + 2

    return ans