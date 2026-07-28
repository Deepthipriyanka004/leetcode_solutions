# Last updated: 7/28/2026, 8:06:39 PM
1class Solution:
2    def smallestPalindrome(self, s: str) -> str:
3        n = len(s)
4        half = ''.join(sorted(s[:n // 2]))
5        middle = s[n // 2] if n % 2 else ""
6        return half + middle + half[::-1]