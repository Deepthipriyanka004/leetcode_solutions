// Last updated: 4/30/2026, 8:57:59 PM
1class Solution {
2public:
3    int maxPathScore(vector<vector<int>>& grid, int k) {
4        int m=grid.size(),n=grid[0].size();
5        vector<vector<vector<int>>> dp(m,vector<vector<int>>(n,vector<int>(k+1,-1)));
6        dp[0][0][0]=0;
7        for(int i=0;i<m;i++){
8            for(int j=0;j<n;j++){
9                for(int c=0;c<=k;c++){
10                    if(dp[i][j][c]==-1){
11                        continue;
12                    }
13                    // move down
14                    if(i+1<m){
15                        int val=grid[i+1][j];
16                        int cost=(val==0?0:1);
17                        int nc=c+cost;
18                        if(nc<=k){
19                            dp[i+1][j][nc]=max(dp[i+1][j][nc],dp[i][j][c]+val);
20                        }
21                    }
22                    // move right
23                    if(j+1<n){
24                        int val=grid[i][j+1];
25                        int cost=(val==0?0:1);
26                        int nc=c+cost;
27                        if(nc<=k){
28                            dp[i][j+1][nc]=max(dp[i][j+1][nc],dp[i][j][c]+val);
29                        }
30                    }
31                }
32            }
33        }
34        int ans=-1;
35        for(int c=0;c<=k;c++){
36            ans=max(ans,dp[m-1][n-1][c]);
37        }
38        return ans;
39    }
40};