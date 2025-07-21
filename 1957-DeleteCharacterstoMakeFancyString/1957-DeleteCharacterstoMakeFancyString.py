# Last updated: 7/21/2025, 2:15:22 PM
class Solution:
  def makeFancyString(self, s: str) -> str:
    ans = []
    for c in s:
      if len(ans) < 2 or ans[-1] != c or ans[-2] != c:
        ans.append(c)
    return ''.join(ans)