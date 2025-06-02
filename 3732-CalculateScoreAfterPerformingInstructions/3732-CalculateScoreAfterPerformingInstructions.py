# Last updated: 6/2/2025, 6:29:46 PM
from typing import List

class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        visited = set()
        score = 0
        i = 0
        n = len(instructions)

        while 0 <= i < n and i not in visited:
            visited.add(i)
            if instructions[i] == "add":
                score += values[i]
                i += 1
            elif instructions[i] == "jump":
                i += values[i]

        return score
