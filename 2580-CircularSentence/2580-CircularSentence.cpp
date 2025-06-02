// Last updated: 6/2/2025, 6:32:23 PM
class Solution {
 public:
  bool isCircularSentence(string sentence) {
    for (int i = 0; i < sentence.length(); ++i)
      if (sentence[i] == ' ' && sentence[i - 1] != sentence[i + 1])
        return false;
    return sentence.front() == sentence.back();
  }
};