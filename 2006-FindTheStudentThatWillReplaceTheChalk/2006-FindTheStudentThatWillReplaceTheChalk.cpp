// Last updated: 6/2/2025, 6:34:11 PM
class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        long long s = accumulate(chalk.begin(), chalk.end(), 0LL);
        k %= s;
        for (int i = 0;; ++i) {
            if (k < chalk[i]) {
                return i;
            }
            k -= chalk[i];
        }
    }
};