class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        memo = defaultdict(int)
        coins = set(coins)
        for coin in coins:
            if coin == amount: return 1
            memo[coin] = 1
    
        for value in range(1, amount+1):
            if value in coins: continue
            
            if value not in memo:
                minNumCoins = float('inf')
            else:
                minNumCoins = memo[value]

            for coin in coins:
                if value - coin in memo:
                    minNumCoins = min(memo[value-coin]+1, minNumCoins)
            
            if minNumCoins != float('inf'):
                memo[value] = minNumCoins
        
        
        return memo.get(amount, -1)
