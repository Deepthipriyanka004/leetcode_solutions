# Last updated: 6/2/2025, 6:29:32 PM
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        half = []
        middle = ''

        for ch in sorted(freq.keys()):
            count = freq[ch]
            # Add half the characters to build the first half of the palindrome
            half.append(ch * (count // 2))
            # If there's an odd count, pick the smallest character as middle
            if count % 2 == 1:
                if middle == '' or ch < middle:
                    middle = ch

        first_half = ''.join(half)
        return first_half + middle + first_half[::-1]
