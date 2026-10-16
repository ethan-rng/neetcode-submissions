from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: 
            return 0
        
        # Initialize memo with infinity for all amounts
        memo = {0: 0}  # Base case: 0 coins needed for amount 0
        
        for value in range(1, amount + 1):
            memo[value] = float('inf')  # Initialize with "unreachable"
            for coin in coins:
                if value - coin >= 0 and value - coin in memo:
                    memo[value] = min(memo[value], memo[value - coin] + 1)
        
        return memo[amount] if memo[amount] != float('inf') else -1
