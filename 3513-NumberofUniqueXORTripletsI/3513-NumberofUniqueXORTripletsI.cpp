// Last updated: 7/23/2026, 11:52:34 PM
1class Solution {
2public:
3    int uniqueXorTriplets(vector<int>& nums) {
4        int n = nums.size();
5        if (n <= 2) {
6            return n;
7        }
8        int ans = 1;
9        while (ans <= n) {
10            ans <<= 1;
11        }
12        return ans;
13    }
14};