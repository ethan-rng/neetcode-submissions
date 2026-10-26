class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        memo = defaultdict(int)

        def dfs(l: int, r: int):
            # Empty range
            if l > r:
                return 0

            # Memo
            if (l, r) in memo:
                return memo[(l, r)]

            leftKeepVal = nums[l - 1]
            rightKeepVal = nums[r + 1]

            # Base Case
            if l == r:
                return leftKeepVal * nums[l] * rightKeepVal

            # Keep number
            maxVal = 0
            for i in range(l, r + 1):
                sides = dfs(l, i - 1) + dfs(i + 1, r)
                maxVal = max(leftKeepVal * nums[i] * rightKeepVal + sides, maxVal)

            memo[(l, r)] = maxVal
            return memo[(l, r)]

        return dfs(1, n - 2)