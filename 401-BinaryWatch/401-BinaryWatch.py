# Last updated: 2/17/2026, 10:38:17 AM
1class Solution:
2  def readBinaryWatch(self, turnedOn: int) -> list[str]:
3    ans = []
4    hours = [1, 2, 4, 8]
5    minutes = [1, 2, 4, 8, 16, 32]
6
7    def dfs(turnedOn: int, s: int, h: int, m: int) -> None:
8      if turnedOn == 0:
9        time = str(h) + ":" + (str(m).zfill(2))
10        ans.append(time)
11        return
12
13      for i in range(s, len(hours) + len(minutes)):
14        if i < 4 and h + hours[i] < 12:
15          dfs(turnedOn - 1, i + 1, h + hours[i], m)
16        elif i >= 4 and m + minutes[i - 4] < 60:
17          dfs(turnedOn - 1, i + 1, h, m + minutes[i - 4])
18
19    dfs(turnedOn, 0, 0, 0)
20    return ans