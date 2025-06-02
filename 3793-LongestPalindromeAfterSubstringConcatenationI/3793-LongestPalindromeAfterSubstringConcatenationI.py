# Last updated: 6/2/2025, 6:29:41 PM
from typing import List

class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        max_length = 1  # Single character is always a palindrome
        
        # Try all possible substrings from s and t
        for i in range(len(s) + 1):
            for j in range(i, len(s) + 1):
                sub_s = s[i:j]
                for k in range(len(t) + 1):
                    for l in range(k, len(t) + 1):
                        sub_t = t[k:l]
                        combined = sub_s + sub_t
                        if is_palindrome(combined):
                            max_length = max(max_length, len(combined))
        
        return max_length

# Example test cases
sol = Solution()
print(sol.longestPalindrome("a", "a"))      # Output: 2
print(sol.longestPalindrome("abc", "def"))  # Output: 1
print(sol.longestPalindrome("b", "aaaa"))   # Output: 4
print(sol.longestPalindrome("abcde", "ecdba"))  # Output: 5
