// Last updated: 4/8/2026, 12:00:11 PM
1class Solution {
2public:
3    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
4        int n=nums.size(),mod=1e9+7;
5        for(auto q:queries){
6            int l=q[0],r=q[1],k=q[2],v=q[3];
7            for(int i=l;i<=r;i+=k){
8                nums[i]=1ll*nums[i]*v%mod;
9            }
10        }
11        int res=0;
12        for(auto x:nums){
13            res^=x;
14        }
15        return res;
16    }
17};