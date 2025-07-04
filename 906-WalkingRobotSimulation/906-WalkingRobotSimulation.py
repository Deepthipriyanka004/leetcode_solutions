# Last updated: 6/2/2025, 6:36:32 PM
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        px, py, pd = 0, 0, 0
        obstacles = set([tuple(t) for t in obstacles])
        ans = 0
        for c in commands:
            if c == -1:
                pd = (pd + 1) % 4
            elif c == -2:
                pd = (pd - 1) % 4
            else:
                for _ in range(c):
                    if (px + dxy[pd][0], py + dxy[pd][1]) in obstacles:
                        break
                    px, py = px + dxy[pd][0], py + dxy[pd][1]
                    ans = max(ans, px * px + py * py)
        return ans