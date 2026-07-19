# Last updated: 7/19/2026, 9:35:53 AM
1class Solution:
2  def smallestSubsequence(self, text: str) -> str:
3    ans = []
4    count = collections.Counter(text)
5    used = [False] * 26
6
7    for c in text:
8      count[c] -= 1
9      if used[ord(c) - ord('a')]:
10        continue
11      while ans and ans[-1] > c and count[ans[-1]] > 0:
12        used[ord(ans[-1]) - ord('a')] = False
13        ans.pop()
14      ans.append(c)
15      used[ord(ans[-1]) - ord('a')] = True
16
17    return ''.join(ans)