// Last updated: 2/4/2026, 4:42:46 PM
1class Solution {
2public:
3    long long maxSumTrionic(vector<int>& nums) {
4        int n = nums.size();
5        int i = 0;
6        long long ans = LLONG_MIN;
7        while (i < n) {
8            int l = i;
9            i += 1;
10            while (i < n && nums[i - 1] < nums[i]) {
11                i += 1;
12            }
13            if (i == l + 1) {
14                continue;
15            }
16
17            int p = i - 1;
18            long long s = nums[p - 1] + nums[p];
19            while (i < n && nums[i - 1] > nums[i]) {
20                s += nums[i];
21                i += 1;
22            }
23            if (i == p + 1 || i == n || nums[i - 1] == nums[i]) {
24                continue;
25            }
26
27            int q = i - 1;
28            s += nums[i];
29            i += 1;
30            long long mx = 0, t = 0;
31            while (i < n && nums[i - 1] < nums[i]) {
32                t += nums[i];
33                i += 1;
34                mx = max(mx, t);
35            }
36            s += mx;
37
38            mx = 0, t = 0;
39            for (int j = p - 2; j >= l; j--) {
40                t += nums[j];
41                mx = max(mx, t);
42            }
43            s += mx;
44
45            ans = max(ans, s);
46            i = q;
47        }
48        return ans;
49    }
50};