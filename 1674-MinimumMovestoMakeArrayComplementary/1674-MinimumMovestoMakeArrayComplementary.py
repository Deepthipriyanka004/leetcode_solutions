# Last updated: 5/13/2026, 10:08:06 AM
1class Solution:
2  def minMoves(self, nums: list[int], limit: int) -> int:
3    n = len(nums)
4    ans = n
5    # delta[i] := the number of moves needed when target goes from i - 1 to i
6    delta = [0] * (limit * 2 + 2)
7
8    for i in range(n // 2):
9      a = nums[i]
10      b = nums[n - 1 - i]
11      delta[min(a, b) + 1] -= 1
12      delta[a + b] -= 1
13      delta[a + b + 1] += 1
14      delta[max(a, b) + limit + 1] += 1
15
16    # Initially, we need `moves` when the target is 2.
17    moves = n
18    for i in range(2, limit * 2 + 1):
19      moves += delta[i]
20      ans = min(ans, moves)
21
22    return ans