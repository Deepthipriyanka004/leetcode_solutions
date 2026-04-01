# Last updated: 4/1/2026, 9:05:53 PM
1from dataclasses import dataclass
2
3
4@dataclass
5class Robot:
6  index: int
7  position: int
8  health: int
9  direction: str
10
11
12class Solution:
13  def survivedRobotsHealths(
14      self,
15      positions: list[int],
16      healths: list[int],
17      directions: str,
18  ) -> list[int]:
19    robots = sorted([Robot(index, position, health, direction)
20                     for index, (position, health, direction) in
21                     enumerate(zip(positions, healths, directions))],
22                    key=lambda x: x.position)
23    stack: list[Robot] = []  # running robots
24
25    for robot in robots:
26      if robot.direction == 'R':
27        stack.append(robot)
28        continue
29      # Collide with robots going right if any.
30      while stack and stack[-1].direction == 'R' and robot.health > 0:
31        if stack[-1].health == robot.health:
32          stack.pop()
33          robot.health = 0
34        elif stack[-1].health < robot.health:
35          stack.pop()
36          robot.health -= 1
37        else:  # stack[-1].health > robot.health
38          stack[-1].health -= 1
39          robot.health = 0
40      if robot.health > 0:
41        stack.append(robot)
42
43    stack.sort(key=lambda robot: robot.index)
44    return [robot.health for robot in stack]