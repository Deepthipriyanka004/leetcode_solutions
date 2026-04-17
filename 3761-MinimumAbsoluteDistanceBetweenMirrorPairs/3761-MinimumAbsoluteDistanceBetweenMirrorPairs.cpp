// Last updated: 4/17/2026, 7:47:52 PM
1class Solution {
2public:
3    int reverseNum(int x) {
4        int y=0;
5        while(x>0){
6            y=(y*10)+(x%10);
7            x/=10;
8        }
9        return y;
10    };
11    int minMirrorPairDistance(vector<int>& nums) {
12        int n=nums.size();
13        unordered_map<int,int> prev;
14        int ans=n+1;
15        for(int i=0;i<n;i++){
16            int x=nums[i];
17            if(prev.count(x)){
18                ans=min(ans,i-prev[x]);
19            }
20            prev[reverseNum(x)]=i;
21        }
22        return (ans==n+1)?-1:ans;
23    }
24};