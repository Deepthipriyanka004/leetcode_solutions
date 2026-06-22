# Last updated: 6/22/2026, 7:22:21 PM
1class Solution:
2  def maxNumberOfBalloons(self, text: str) -> int:
3    count = collections.Counter(text)
4    return min(
5        count['b'],
6        count['a'],
7        count['l'] // 2, count['o'] // 2, count['n'])