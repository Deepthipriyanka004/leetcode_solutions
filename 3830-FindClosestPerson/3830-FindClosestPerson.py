# Last updated: 6/2/2025, 6:29:26 PM
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist1 = abs(x - z)
        dist2 = abs(y - z)

        if dist1 < dist2:
            return 1
        elif dist2 < dist1:
            return 2
        else:
            return 0
