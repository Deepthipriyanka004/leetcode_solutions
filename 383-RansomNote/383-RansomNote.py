# Last updated: 6/2/2025, 6:37:31 PM
class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    count1 = collections.Counter(ransomNote)
    count2 = collections.Counter(magazine)
    return all(count1[c] <= count2[c] for c in string.ascii_lowercase)