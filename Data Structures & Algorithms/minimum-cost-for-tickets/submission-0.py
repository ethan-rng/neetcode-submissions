class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = defaultdict(int)
        maxDay = max(days)
        days = set(days)
        numDays = [1, 7, 30]

        def dfs(day: int) -> int:
            if day <= 0:
                return 0

            if day in memo: 
                return memo[day]
            
            minCost = float('inf')
            if day in days:
                for i, days_per_ticket in enumerate(numDays):
                    daysLeft = day - days_per_ticket
                    minCost = min(costs[i] + dfs(daysLeft), minCost)
            else:
                minCost = dfs(day - 1)
            
            memo[day] = minCost
            return memo[day]

        print(memo)
        res = dfs(maxDay)
        return res