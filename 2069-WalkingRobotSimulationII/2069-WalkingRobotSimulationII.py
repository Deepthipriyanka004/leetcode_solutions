# Last updated: 4/7/2026, 11:13:28 AM
1class Robot:
2  def __init__(self, width: int, height: int):
3    self.isOrigin = True
4    self.i = 0
5    self.pos = ([((0, 0), 'South')] +
6                [((i, 0), 'East') for i in range(1, width)] +
7                [((width - 1, j), 'North') for j in range(1, height)] +
8                [((i, height - 1), 'West') for i in range(width - 2, -1, -1)] +
9                [((0, j), 'South') for j in range(height - 2, 0, -1)])
10
11  def step(self, num: int) -> None:
12    self.isOrigin = False
13    self.i = (self.i + num) % len(self.pos)
14
15  def getPos(self) -> list[int]:
16    return self.pos[self.i][0]
17
18  def getDir(self) -> str:
19    return 'East' if self.isOrigin else self.pos[self.i][1]