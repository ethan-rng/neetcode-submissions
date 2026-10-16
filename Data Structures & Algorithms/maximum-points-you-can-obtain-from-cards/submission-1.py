class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)

        total = sum(cardPoints)
        n = len(cardPoints) - k # length of the sliding window
        l, r = 0, n - 1
        minWindow = 0
        runningWindowCount = 0

        for i in range(n):
            minWindow += cardPoints[i]
            runningWindowCount += cardPoints[i]

        while r < len(cardPoints):
            if l != 0:
                runningWindowCount += cardPoints[r]
            print(l, minWindow, runningWindowCount, r)
            minWindow = min(
                minWindow,
                runningWindowCount
            )

            runningWindowCount -= cardPoints[l]
            l += 1
            r += 1

        
        print(minWindow)
        return sum(cardPoints) - minWindow
