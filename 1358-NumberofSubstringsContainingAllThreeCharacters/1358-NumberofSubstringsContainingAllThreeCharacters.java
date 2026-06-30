// Last updated: 6/30/2026, 7:13:14 PM
1class Solution {
2  // Similar to 3. Longest SubString Without Repeating Characters
3  public int numberOfSubstrings(String s) {
4    int ans = 0;
5    int[] count = new int[3];
6
7    int l = 0;
8    for (final char c : s.toCharArray()) {
9      ++count[c - 'a'];
10      while (count[0] > 0 && count[1] > 0 && count[2] > 0)
11        --count[s.charAt(l++) - 'a'];
12      // s[0..r], s[1..r], ..., s[l - 1..r] are satified strings.
13      ans += l;
14    }
15
16    return ans;
17  }
18}