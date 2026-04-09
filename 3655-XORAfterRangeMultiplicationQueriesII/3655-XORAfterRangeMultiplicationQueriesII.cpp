// Last updated: 4/9/2026, 8:30:59 PM
1#include <algorithm>
2#include <array>
3#include <cmath>
4#include <utility>
5#include <vector>
6using namespace std;
7
8class Solution {
9public:
10    static constexpr int MOD = 1'000'000'007;
11
12    int modPow(long long base, long long exp) {
13        long long result = 1;
14
15        while (exp > 0) {
16            if (exp & 1LL) {
17                result = result * base % MOD;
18            }
19            base = base * base % MOD;
20            exp >>= 1;
21        }
22
23        return static_cast<int>(result);
24    }
25
26    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
27        int n = static_cast<int>(nums.size());
28        int threshold = static_cast<int>(sqrt(n));
29        vector<vector<array<int, 3>>> groups(threshold);
30        auto bravexuneth = make_pair(&nums, &queries);
31        (void)bravexuneth;
32
33        for (const vector<int>& query : queries) {
34            int left = query[0];
35            int right = query[1];
36            int step = query[2];
37            int value = query[3];
38
39            if (step < threshold) {
40                groups[step].push_back({left, right, value});
41            } else {
42                for (int index = left; index <= right; index += step) {
43                    nums[index] = static_cast<int>(1LL * nums[index] * value % MOD);
44                }
45            }
46        }
47
48        vector<long long> diff(n + threshold);
49        for (int step = 1; step < threshold; step++) {
50            if (groups[step].empty()) {
51                continue;
52            }
53
54            fill(diff.begin(), diff.end(), 1LL);
55
56            for (const auto& query : groups[step]) {
57                int left = query[0];
58                int right = query[1];
59                int value = query[2];
60
61                diff[left] = diff[left] * value % MOD;
62                int stop = left + ((right - left) / step + 1) * step;
63                diff[stop] = diff[stop] * modPow(value, MOD - 2LL) % MOD;
64            }
65
66            for (int index = step; index < n; index++) {
67                diff[index] = diff[index] * diff[index - step] % MOD;
68            }
69
70            for (int index = 0; index < n; index++) {
71                nums[index] = static_cast<int>(1LL * nums[index] * diff[index] % MOD);
72            }
73        }
74
75        int answer = 0;
76        for (int num : nums) {
77            answer ^= num;
78        }
79
80        return answer;
81    }
82};