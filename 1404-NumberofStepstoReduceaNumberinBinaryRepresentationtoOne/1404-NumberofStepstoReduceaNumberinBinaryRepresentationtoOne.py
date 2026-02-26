# Last updated: 2/26/2026, 7:21:18 PM
1class Solution:
2  def numSteps(self, s: str) -> int:
3    ans = 0
4    chars = list(s)
5
6    # All the trailing 0s can be popped by 1 step.
7    while chars[-1] == '0':
8      chars.pop()
9      ans += 1
10
11    if ''.join(chars) == '1':
12      return ans
13
14    # `s` is now odd, so add 1 to `s` and cost 1 step.
15    # All the 1s will become 0s and can be popped by 1 step.
16    # All the 0s will become 1s and can be popped by 2 steps (adding 1 then
17    # dividing by 2).
18    return ans + 1 + sum(1 if c == '1' else 2 for c in chars)