# Last updated: 12/27/2025, 8:49:56 PM
1class Solution:
2  def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
3    count = [0] * n
4
5    meetings.sort()
6
7    occupied = []  # (endTime, roomId)
8    availableRoomIds = [i for i in range(n)]
9    heapq.heapify(availableRoomIds)
10
11    for start, end in meetings:
12      # Push meetings ending before this `meeting` in occupied to the
13      # `availableRoomsIds`.
14      while occupied and occupied[0][0] <= start:
15        heapq.heappush(availableRoomIds, heapq.heappop(occupied)[1])
16      if availableRoomIds:
17        roomId = heapq.heappop(availableRoomIds)
18        count[roomId] += 1
19        heapq.heappush(occupied, (end, roomId))
20      else:
21        newStart, roomId = heapq.heappop(occupied)
22        count[roomId] += 1
23        heapq.heappush(occupied, (newStart + (end - start), roomId))
24
25    return count.index(max(count))