# Last updated: 6/4/2025, 10:08:15 AM
class Solution:
  def answerString(self, word: str, numFriends: int) -> str:
    if numFriends == 1:
      return word
    s = self._lastSubstring(word)
    sz = len(word) - numFriends + 1
    return s[:min(len(s), sz)]

  # Same as 1163. Last Substring in Lexicographical Order
  def _lastSubstring(self, s: str) -> str:
    i = 0
    j = 1
    k = 0  # the number of the same letters of s[i..n) and s[j..n)

    while j + k < len(s):
      if s[i + k] == s[j + k]:
        k += 1
      elif s[i + k] > s[j + k]:
        # Skip s[j..j + k) and advance to s[j + k + 1] to find a possible
        # lexicographically larger substring since s[i..i + k) == s[j..j + k)
        # and s[i + k] > s[j + k).
        j = j + k + 1
        k = 0
      else:
        # Skip s[i..i + k) and advance to s[i + k + 1] or s[j] to find a
        # possible lexicographically larger substring since
        # s[i..i + k) == s[j..j + k) and s[i + k] < s[j + k).
        # Note that it's unnecessary to explore s[i + k + 1..j) if
        # i + k + 1 < j since they are already explored by j.
        i = max(i + k + 1, j)
        j = i + 1
        k = 0

    return s[i:]