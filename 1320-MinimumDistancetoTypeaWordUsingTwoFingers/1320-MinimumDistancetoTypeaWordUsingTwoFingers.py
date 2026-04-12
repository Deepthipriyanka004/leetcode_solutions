# Last updated: 4/12/2026, 11:26:00 AM
1class Solution:
2  def minimumDistance(self, word: str) -> int:
3    def dist(a: int, b: int) -> int:
4      if a == 26:  # the first hovering state
5        return 0
6      x1, y1 = a // 6, a % 6
7      x2, y2 = b // 6, b % 6
8      return abs(x1 - x2) + abs(y1 - y2)
9
10    @functools.lru_cache(None)
11    def dp(i: int, j: int, k: int) -> int:
12      """
13      Returns the minimum distance to type the `word`, where the left finger is
14      on the i-th letter, the right finger is on the j-th letter, and the
15      words[0..k) have been written.
16      """
17      if k == len(word):
18        return 0
19      nxt = ord(word[k]) - ord('A')
20      moveLeft = dist(i, nxt) + dp(nxt, j, k + 1)
21      moveRight = dist(j, nxt) + dp(i, nxt, k + 1)
22      return min(moveLeft, moveRight)
23
24    return dp(26, 26, 0)