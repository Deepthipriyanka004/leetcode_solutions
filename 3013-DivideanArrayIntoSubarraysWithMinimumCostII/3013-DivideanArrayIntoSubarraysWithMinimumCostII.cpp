// Last updated: 2/2/2026, 10:42:27 AM
1class Solution {
2 public:
3  long long minimumCost(vector<int>& nums, int k, int dist) {
4    // Equivalently, the problem is to find nums[0] + the minimum sum of the top
5    // k - 1 numbers in nums[i..i + dist], where i > 0 and i + dist < n.
6    long windowSum = 0;
7    multiset<int> selected;
8    multiset<int> candidates;
9
10    for (int i = 1; i <= dist + 1; ++i) {
11      windowSum += nums[i];
12      selected.insert(nums[i]);
13    }
14
15    windowSum = balance(windowSum, selected, candidates, k);
16    long minWindowSum = windowSum;
17
18    for (int i = dist + 2; i < nums.size(); ++i) {
19      const int outOfScope = nums[i - dist - 1];
20      if (selected.find(outOfScope) != selected.end()) {
21        windowSum -= outOfScope;
22        selected.erase(selected.find(outOfScope));
23      } else {
24        candidates.erase(candidates.find(outOfScope));
25      }
26      if (nums[i] < *selected.rbegin()) {  // nums[i] is a better number.
27        windowSum += nums[i];
28        selected.insert(nums[i]);
29      } else {
30        candidates.insert(nums[i]);
31      }
32      windowSum = balance(windowSum, selected, candidates, k);
33      minWindowSum = min(minWindowSum, windowSum);
34    }
35
36    return nums[0] + minWindowSum;
37  }
38
39 private:
40  // Returns the updated `windowSum` by balancing the multiset `selected` to
41  // keep the top k - 1 numbers.
42  long balance(long windowSum, multiset<int>& selected,
43               multiset<int>& candidates, int k) {
44    while (selected.size() < k - 1) {
45      const int minCandidate = *candidates.begin();
46      windowSum += minCandidate;
47      selected.insert(minCandidate);
48      candidates.erase(candidates.find(minCandidate));
49    }
50    while (selected.size() > k - 1) {
51      const int maxSelected = *selected.rbegin();
52      windowSum -= maxSelected;
53      selected.erase(selected.find(maxSelected));
54      candidates.insert(maxSelected);
55    }
56    return windowSum;
57  }
58};