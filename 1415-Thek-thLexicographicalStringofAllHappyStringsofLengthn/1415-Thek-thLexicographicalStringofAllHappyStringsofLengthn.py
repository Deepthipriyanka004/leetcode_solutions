# Last updated: 3/14/2026, 12:32:22 PM
1class Solution:
2  def getHappyString(self, n: int, k: int) -> str:
3    nextLetters = {'a': 'bc', 'b': 'ac', 'c': 'ab'}
4    q = collections.deque(['a', 'b', 'c'])
5
6    while len(q[0]) != n:
7      u = q.popleft()
8      for nextLetter in nextLetters[u[-1]]:
9        q.append(u + nextLetter)
10
11    return '' if len(q) < k else q[k - 1]