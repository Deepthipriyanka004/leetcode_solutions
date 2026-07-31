# Last updated: 7/31/2026, 6:41:18 AM
1class Solution:
2  def minimumPushes(self, word: str) -> int:
3    freqs = sorted(collections.Counter(word).values(), reverse=True)
4    return sum(freq * (i // 8 + 1) for i, freq in enumerate(freqs))