class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(int)
        coins = set(coins)

        if amount == 0: return 0
        if len(coins) == 0: return -1

        def helper(target: int) -> int:
            # Base Case = found min
            if target in coins:
                return 1
                        
            minAmount = float('inf')
            for coin in coins:
                if target in memo:
                    return memo[target]

                if target - coin >= 0:
                    res = helper(target - coin)
                else:
                    res = float('inf')
                
                minAmount = min(minAmount, res)

            memo[target] = minAmount + 1
            return minAmount + 1    

        res = helper(amount)
        return -1 if res == float('inf') else res