class Solution:
    def climbStairs(self, n: int) -> int:   
        output = 0 
        memo = {}

        def checkTotal(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            
            memo[n] =  checkTotal(n-1) + checkTotal(n-2)
            return memo[n]

        
        return checkTotal(n)