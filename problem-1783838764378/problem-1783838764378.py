# Last updated: 7/12/2026, 12:16:04 PM
1class Solution:
2    def arrayRankTransform(self, arr: list[int]) -> list[int]:
3        rank = {}
4
5        for a in sorted(arr):
6            if a not in rank:
7                rank[a] = len(rank) + 1
8
9        return list(map(rank.get, arr))