# Last updated: 6/2/2025, 6:34:59 PM
class Solution:
  def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    words = sentence.split()

    for i, word in enumerate(words):
      if word.startswith(searchWord):
        return i + 1

    return -1