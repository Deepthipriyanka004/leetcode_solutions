# Last updated: 7/19/2025, 12:26:02 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        cleaned = [ch.lower() for ch in s if ch.isalnum()]
        
        start, end = 0, len(cleaned) - 1
        while start < end:
            if cleaned[start] != cleaned[end]:
                return False
            start += 1
            end -= 1
        return True
