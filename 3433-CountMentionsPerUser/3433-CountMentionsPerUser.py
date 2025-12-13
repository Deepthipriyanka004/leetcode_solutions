# Last updated: 12/13/2025, 9:43:47 AM
1from dataclasses import dataclass
2
3
4@dataclass(frozen=True)
5class OfflineUser:
6  returnTimestamp: int
7  userId: int
8
9  def __lt__(self, other):
10    return self.returnTimestamp < other.returnTimestamp
11
12
13class Solution:
14  def countMentions(
15      self,
16      numberOfUsers: int,
17      events: list[list[str]]
18  ) -> list[int]:
19    ans = [0] * numberOfUsers
20    online = [True] * numberOfUsers
21    offlineQueue = []  # min-heap to track users that are offline
22    allMentionsCount = 0
23
24    events.sort(key=lambda x: (int(x[1]), -ord(x[0][0])))
25
26    for eventType, t, messageContent in events:
27      timestamp = int(t)
28      # Bring users back online if their offline period has ended.
29      while offlineQueue and offlineQueue[0].returnTimestamp <= timestamp:
30        user = heapq.heappop(offlineQueue)
31        online[user.userId] = True
32      if eventType == "MESSAGE":
33        match messageContent:
34          case "ALL":
35            allMentionsCount += 1
36          case "HERE":
37            for userId in range(numberOfUsers):
38              if online[userId]:
39                ans[userId] += 1
40          case _:
41            for userId in [int(part[2:]) for part in messageContent.split()]:
42              ans[userId] += 1
43      elif eventType == "OFFLINE":
44        userId = int(messageContent)
45        online[userId] = False
46        # Add to queue to bring back online after 60 units.
47        heapq.heappush(offlineQueue, OfflineUser(timestamp + 60, userId))
48
49    # Add the "ALL" mentions to all users.
50    for userId in range(numberOfUsers):
51      ans[userId] += allMentionsCount
52    return ans