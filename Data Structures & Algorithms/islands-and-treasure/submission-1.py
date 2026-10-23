class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        Y, X = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = deque([])
        INF = 2 ** 31 - 1

        # find islands
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 0:
                    queue.append((y, x))

        seen = set()
        roundNum = 0

        # Run BFS
        while queue:
            currRound = len(queue)
            roundNum += 1

            for _ in range(currRound):    
                y, x = queue.popleft()
                cell = grid[y][x]

                # Add neighbors
                for yOffset, xOffset in dirs:
                    idxY, idxX = y + yOffset, x + xOffset

                    if idxX < 0 or idxY < 0: continue
                    if idxX >= X or idxY >= Y: continue
                    if (idxY, idxX) in seen: continue
                    if grid[idxY][idxX] == -1: continue

                    if grid[idxY][idxX] != 0:
                        grid[idxY][idxX] = roundNum

                    queue.append((idxY, idxX))
                    seen.add((idxY, idxX))


                    





