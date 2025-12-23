// Last updated: 12/23/2025, 1:50:05 PM
1struct Event {
2  int time;
3  int value;
4  bool isStart;
5};
6
7class Solution {
8 public:
9  int maxTwoEvents(vector<vector<int>>& events) {
10    int ans = 0;
11    int maxValue = 0;
12    vector<Event> evts;
13
14    for (const vector<int>& event : events) {
15      const int start = event[0];
16      const int end = event[1];
17      const int value = event[2];
18      evts.emplace_back(start, value, true);
19      evts.emplace_back(end + 1, value, false);
20    }
21
22    ranges::sort(evts, ranges::less{}, [](const Event& evt) {
23      return pair<int, bool>{evt.time, evt.isStart};
24    });
25
26    for (const auto& [_, value, isStart] : evts)
27      if (isStart)
28        ans = max(ans, value + maxValue);
29      else
30        maxValue = max(maxValue, value);
31
32    return ans;
33  }
34};