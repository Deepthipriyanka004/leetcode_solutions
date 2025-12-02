// Last updated: 12/2/2025, 9:15:03 AM
1class Solution {
2public:
3    int countTrapezoids(vector<vector<int>>& points) {
4        unordered_map<int,int> mpp;
5        const int mod=1e9+7;
6        long long ans=0,sum=0;
7        for(auto& point:points){
8            mpp[point[1]]++;
9        }
10        for(auto& [it,val]:mpp){
11            long long edge=(long long)val*(val-1)/2;
12            ans+=edge*sum;
13            sum+=edge;
14        }
15        return ans%mod;
16    }
17};