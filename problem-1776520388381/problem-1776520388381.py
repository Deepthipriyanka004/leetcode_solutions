# Last updated: 4/18/2026, 7:23:08 PM
1class Solution:
2    def mirrorDistance(self, n: int) -> int:
3        return abs(n - int(str(n)[::-1]))