# Last updated: 1/12/2026, 7:57:45 PM
1class Solution:
2    def minTimeToVisitAllPoints(self, points):
3        ans = 0
4        
5        for i in range(1, len(points)):
6            ans += max(abs(points[i][0] - points[i-1][0]),
7                       abs(points[i][1] - points[i-1][1]))
8        
9        return ans
10