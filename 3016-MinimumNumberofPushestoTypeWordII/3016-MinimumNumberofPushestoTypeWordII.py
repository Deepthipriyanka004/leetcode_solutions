# Last updated: 7/31/2026, 6:42:29 AM
1class Solution:
2  # Same as 3014. Minimum Number of Pushes to Type Word I
3  def minimumPushes(self, word: str) -> int:
4    freqs = sorted(collections.Counter(word).values(), reverse=True)
5    return sum(freq * (i // 8 + 1) for i, freq in enumerate(freqs))