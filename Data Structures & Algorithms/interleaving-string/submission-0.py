class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        S1, S2, S3 = len(s1), len(s2), len(s3)
        if S1 + S2 != S3:
            return False

        def dfs(i: int, j: int, k: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            if i == S1 and j == S2:
                return True

            c1 = s1[i] if i < S1 else None
            c2 = s2[j] if j < S2 else None
            c3 = s3[k]

            if c1 == c3 and c2 == c3:
                memo[(i, j)] = dfs(i, j + 1, k + 1) or dfs(i + 1, j, k + 1)
            elif c1 == c3:
                memo[(i, j)] = dfs(i + 1, j, k + 1)
            elif c2 == c3:
                memo[(i, j)] = dfs(i, j + 1, k + 1)
            else:
                memo[(i, j)] = False
            return memo[(i, j)]

        return dfs(0, 0, 0)