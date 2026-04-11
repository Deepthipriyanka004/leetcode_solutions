// Last updated: 4/11/2026, 11:30:09 PM
1#include <algorithm>
2#include <climits>
3#include <vector>
4using namespace std;
5
6class Solution {
7public:
8    int minimumDistance(vector<int>& nums) {
9        int n = nums.size();
10        vector<int> next(n, -1);
11        vector<int> last(n + 1, -1);
12
13        for (int i = n - 1; i >= 0; i--) {
14            int value = nums[i];
15            next[i] = last[value];
16            last[value] = i;
17        }
18
19        int answer = INT_MAX;
20
21        for (int i = 0; i < n; i++) {
22            int second = next[i];
23            if (second == -1) {
24                continue;
25            }
26
27            int third = next[second];
28            if (third == -1) {
29                continue;
30            }
31
32            answer = min(answer, (third - i) * 2);
33        }
34
35        return answer == INT_MAX ? -1 : answer;
36    }
37};