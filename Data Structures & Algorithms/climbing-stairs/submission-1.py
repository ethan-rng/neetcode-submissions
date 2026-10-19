class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def recursiveClimb(curr_n: int) -> int:
            # Base Case
            if curr_n == 1 or curr_n == 2:
                return curr_n
            
            # Memo Access
            if curr_n in memo:
                return memo[curr_n]

            res = recursiveClimb(curr_n - 1) + recursiveClimb(curr_n - 2)
            # Caching into Memo
            memo[curr_n] = res

            return res

        return recursiveClimb(n)