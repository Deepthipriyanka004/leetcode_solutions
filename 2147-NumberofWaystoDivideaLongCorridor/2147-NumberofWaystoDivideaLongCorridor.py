# Last updated: 12/14/2025, 11:47:51 AM
1class Solution:
2  def numberOfWays(self, corridor: str) -> int:
3    MOD = 1_000_000_007
4    ans = 1
5    prevSeat = -1
6    numSeats = 0
7
8    for i, c in enumerate(corridor):
9      if c == 'S':
10        numSeats += 1
11        if numSeats > 2 and numSeats % 2 == 1:
12          ans = ans * (i - prevSeat) % MOD
13        prevSeat = i
14
15    return ans if numSeats > 1 and numSeats % 2 == 0 else 0