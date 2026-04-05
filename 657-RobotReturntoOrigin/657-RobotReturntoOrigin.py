# Last updated: 4/5/2026, 10:16:57 AM
1class Solution:
2  def judgeCircle(self, moves: str) -> bool:
3    return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')