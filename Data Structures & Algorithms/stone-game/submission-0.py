class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def dfs(l: int, r: int) -> int:
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]

            isAliceTurn = (r - l) % 2

            # Person Takes Left
            leftPile = piles[l] if isAliceTurn else 0
            rightPile = piles[r] if isAliceTurn else 0

            res = max(leftPile + dfs(l + 1, r), rightPile + dfs(l, r -1))
            memo[(l, r)] = res

            return res
        
        alice = dfs(0, len(piles) - 1)
        bob = sum(piles) - alice
        return alice > bob