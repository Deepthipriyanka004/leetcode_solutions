// Last updated: 8/1/2026, 4:01:56 PM
1class Solution {
2public:
3    /*
4    we have two choices either to choose the first or last so we will choose the
5    element which gives us the best result ans the other one will choose a
6    number which will be maximum of his choice. if we choose the first number i
7    then opponent can choose either i+1 or jth number then he has two choices if
8    i+1 we get i+2,j and if he chooses jth we get i+1,j-1 . after what he
9    chooses he will try to give us as minimum result as possible. if we choose
10    last number then the other player will get i,j-1 the he will choose either
11    i+1 or j-1 then we get i+1,j-1 or i,j-2 and we will have minimum after these
12    choices
13    */
14    int f(vector<int>& nums, int i, int j, vector<vector<int>>& dp) {
15        if (i > j)
16            return 0;
17        if (i == j)
18            return nums[i];
19        if (dp[i][j] != -1)
20            return dp[i][j];
21        int a = nums[i] + min(f(nums, i + 2, j, dp), f(nums, i + 1, j - 1, dp));
22        int b = nums[j] + min(f(nums, i, j - 2, dp), f(nums, i + 1, j - 1, dp));
23        dp[i][j] = max(a, b);
24        return dp[i][j];
25    }
26    bool predictTheWinner(vector<int>& nums) {
27        int n = nums.size();
28        vector<vector<int>> dp(n, vector<int>(n, -1));
29        int sum = 0;
30        for (auto i : nums) {
31            sum += i;
32        }
33        int ans = f(nums, 0, n - 1, dp);
34        int ans2 = sum - ans;
35        return ans >= ans2;
36    }
37};