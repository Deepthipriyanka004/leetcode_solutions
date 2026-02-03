// Last updated: 2/3/2026, 8:24:55 PM
1class Solution {
2public:
3    bool isTrionic(vector<int>& nums) {
4        int n=nums.size(),i=1;
5        while(i<n && nums[i-1]<nums[i]){
6            i++;
7        }
8        int p=i-1;
9        while (i<n && nums[i-1]>nums[i]){
10            i++;
11        }
12        int q=i-1;
13        while(i<n && nums[i-1]<nums[i]){
14            i++;
15        }
16        int flag=i-1;
17        return (p!=0) && (q!=p) && (flag==n-1 && flag!=q);
18    }
19};