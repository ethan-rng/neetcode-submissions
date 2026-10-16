class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        color = '8' # random non color char
        totalTime = 0

        # Per boundary
        maxTime = -float('inf')
        totalColorTime = 0

        for i in range(len(colors)):
            c = colors[i]
            t = neededTime[i]

            # Adj
            if c == color:
                maxTime = max(maxTime, t)
                totalColorTime += t
                continue

            # Crossing Boundary
            if c != color:
                maxTime = 0 if maxTime == -float('inf') else maxTime
                totalTime += totalColorTime - maxTime

                maxTime = t
                color = c
                totalColorTime = t
                continue
        
        # Last Boundary Checker
        if colors[-1] == color:
            maxTime = 0 if maxTime == -float('inf') else maxTime
            print(totalColorTime, color)
            totalTime += totalColorTime - maxTime

        return totalTime
