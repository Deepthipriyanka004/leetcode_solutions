// Last updated: 6/2/2025, 6:30:53 PM
class Solution {
public:
    int maximumLength(string s) {
        int l{0}, r{1}, n{(int)s.length()};
        array<array<int, 60>, 26> cnt = {};
        int ans{-1};
        while (r <= n) {
            while (r < n and s[r] == s[l])
                r++;
            for (int i{r - 1}; i >= l; i--) {
                int len{i - l + 1};
                cnt[s[l] - 'a'][len] += r - i;
                if (cnt[s[l] - 'a'][len] > 2 && len > ans)
                    ans = len;
            }
            l = r;
            r++;
        }
        return ans;
    }
};