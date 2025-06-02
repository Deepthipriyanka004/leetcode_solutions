// Last updated: 6/2/2025, 6:36:44 PM
class Solution {
 public:
  bool rotateString(string s, string goal) {
    return s.length() == goal.length() && (s + s).find(goal) != string::npos;
  }
};