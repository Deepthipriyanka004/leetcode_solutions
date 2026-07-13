# Last updated: 7/13/2026, 8:31:35 PM
1class Solution:
2  def sequentialDigits(self, low: int, high: int) -> list[int]:
3    ans = []
4    q = collections.deque([num for num in range(1, 10)])
5
6    while q:
7      num = q.popleft()
8      if num > high:
9        return ans
10      if low <= num and num <= high:
11        ans.append(num)
12      lastDigit = num % 10
13      if lastDigit < 9:
14        q.append(num * 10 + lastDigit + 1)
15
16    return ans
17
18
19