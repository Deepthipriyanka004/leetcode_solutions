# Last updated: 6/2/2025, 6:29:23 PM
class Solution:
    def resultingString(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack:
                top = stack[-1]
                diff = abs(ord(ch) - ord(top))
                if diff == 1 or diff == 25:
                    stack.pop()
                    continue
            stack.append(ch)

        return ''.join(stack)
