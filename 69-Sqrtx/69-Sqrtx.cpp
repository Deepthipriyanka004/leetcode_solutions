// Last updated: 6/2/2025, 6:41:02 PM
class Solution {
public:
    int mySqrt(int x) {
        int l = 0, r = x;
        while (l < r) {
            int mid = (l + r + 1ll) >> 1;
            if (mid > x / mid) {
                r = mid - 1;
            } else {
                l = mid;
            }
        }
        return l;
    }
};