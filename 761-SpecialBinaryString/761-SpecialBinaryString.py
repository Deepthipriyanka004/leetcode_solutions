# Last updated: 2/20/2026, 11:20:56 AM
1class Solution:
2  def makeLargestSpecial(self, s: str) -> str:
3    specials = []
4    count = 0
5
6    i = 0
7    for j, c in enumerate(s):
8      count += 1 if c == '1' else -1
9      if count == 0:
10        specials.append(
11            '1' + self.makeLargestSpecial(s[i + 1:j]) + '0')
12        i = j + 1
13
14    return ''.join(sorted(specials)[::-1])