class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Y, X = len(grid), len(grid[0])
        print(Y, X)
        visited = set()
        numIslands = 0
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "0": continue
                if (y, x) in visited: continue

                # BFS part
                queue = deque([(y, x)])
                numIslands += 1

                while queue:
                    newY, newX = queue.popleft()

                    for offsetY, offsetX in dirs:
                        if not(newX + offsetX >= 0 and newX + offsetX < X):
                            continue

                        if not(newY + offsetY >= 0 and newY + offsetY < Y):
                            continue

                        if grid[newY + offsetY][newX + offsetX] != "1": 
                            continue

                        if (newY + offsetY, newX + offsetX) in visited:
                            continue
                            
                        queue.append((newY + offsetY, newX + offsetX))
                        visited.add((newY + offsetY, newX + offsetX))

        
        return numIslands
