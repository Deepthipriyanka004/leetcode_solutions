# Last updated: 9/15/2025, 11:20:12 AM
class Solution:
  def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
    ans = 0
    broken = set(brokenLetters)

    for word in text.split():
      ans += all(c not in broken for c in word)

    return ans