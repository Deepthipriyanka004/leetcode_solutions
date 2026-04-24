# Last updated: 4/24/2026, 8:06:34 PM
1class Solution:
2    def furthestDistanceFromOrigin(self, moves: str) -> int:
3        countL = 0
4        countR = 0
5        countUnderline = 0
6
7        for c in moves:
8            if c == 'L':
9                countL += 1
10            elif c == 'R':
11                countR += 1
12            else:  # c == '_'
13                countUnderline += 1
14
15        return abs(countL - countR) + countUnderline