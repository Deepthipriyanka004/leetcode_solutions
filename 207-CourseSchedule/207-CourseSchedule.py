# Last updated: 6/2/2025, 6:38:27 PM
from enum import Enum


class State(Enum):
  INIT = 0
  VISITING = 1
  VISITED = 2


class Solution:
  def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    states = [State.INIT] * numCourses

    for v, u in prerequisites:
      graph[u].append(v)

    def hasCycle(u: int) -> bool:
      if states[u] == State.VISITING:
        return True
      if states[u] == State.VISITED:
        return False
      states[u] = State.VISITING
      if any(hasCycle(v) for v in graph[u]):
        return True
      states[u] = State.VISITED
      return False

    return not any(hasCycle(i) for i in range(numCourses))