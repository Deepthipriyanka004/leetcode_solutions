# Last updated: 6/5/2026, 8:32:05 PM
1from functools import lru_cache
2
3class Solution:
4    def totalWaviness(self, num1: int, num2: int) -> int:
5
6        def solve(n: int) -> int:
7            if n < 0:
8                return 0
9
10            s = str(n)
11            m = len(s)
12
13            @lru_cache(None)
14            def dp(pos, tight, started, length_state, prev2, prev1):
15                """
16                Returns:
17                    (count_numbers, total_waviness)
18                """
19
20                if pos == m:
21                    return (1, 0)
22
23                limit = int(s[pos]) if tight else 9
24
25                total_count = 0
26                total_wavy = 0
27
28                for d in range(limit + 1):
29                    ntight = tight and (d == limit)
30
31                    # still leading zeros
32                    if not started and d == 0:
33                        cnt, wav = dp(
34                            pos + 1,
35                            ntight,
36                            False,
37                            0,
38                            10,
39                            10
40                        )
41                        total_count += cnt
42                        total_wavy += wav
43
44                    # first non-zero digit
45                    elif not started:
46                        cnt, wav = dp(
47                            pos + 1,
48                            ntight,
49                            True,
50                            1,
51                            10,
52                            d
53                        )
54                        total_count += cnt
55                        total_wavy += wav
56
57                    else:
58                        # currently length = 1
59                        if length_state == 1:
60                            cnt, wav = dp(
61                                pos + 1,
62                                ntight,
63                                True,
64                                2,
65                                prev1,
66                                d
67                            )
68                            total_count += cnt
69                            total_wavy += wav
70
71                        # length >= 2
72                        else:
73                            middle = prev1
74
75                            is_peak = middle > prev2 and middle > d
76                            is_valley = middle < prev2 and middle < d
77                            add = 1 if (is_peak or is_valley) else 0
78
79                            cnt, wav = dp(
80                                pos + 1,
81                                ntight,
82                                True,
83                                2,
84                                prev1,
85                                d
86                            )
87
88                            total_count += cnt
89                            total_wavy += wav + add * cnt
90
91                return (total_count, total_wavy)
92
93            return dp(0, True, False, 0, 10, 10)[1]
94
95        return solve(num2) - solve(num1 - 1)