# Last updated: 1/31/2026, 9:18:14 PM
1class Solution:
2  def nextGreatestLetter(self, letters: list[str], target: str) -> str:
3    l = bisect.bisect_right(range(len(letters)), target,
4                            key=lambda m: letters[m])
5    return letters[l % len(letters)]