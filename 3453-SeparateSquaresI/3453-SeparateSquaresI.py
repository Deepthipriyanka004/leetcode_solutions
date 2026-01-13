# Last updated: 1/13/2026, 9:43:27 AM
1class Solution:
2    def separateSquares(self, squares):
3        halfArea = sum(l * l for _, _, l in squares) / 2.0
4        
5        events = []
6        for x, y, l in squares:
7            events.append((y, True, l))      # start of square
8            events.append((y + l, False, l)) # end of square
9        
10        events.sort()
11        
12        area = 0.0
13        width = 0
14        prevY = events[0][0]
15        
16        for y, isStart, l in events:
17            areaGain = width * (y - prevY)
18            
19            if area + areaGain >= halfArea:
20                # Find exact Y using proportional fill
21                return prevY + (halfArea - area) / width
22            
23            area += areaGain
24            width += l if isStart else -l
25            prevY = y
26        
27        return 0.0   # shouldn't reach here
28