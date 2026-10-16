class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2])
        fruits = set([(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1 or grid[i][j] == 2])
        seen = set()
        total = 0
        Y, X = len(grid), len(grid[0])

        while queue:
            queueLength = len(queue)

            for _ in range(queueLength):
                y, x = queue.popleft()
                fruits.remove((y, x))

                if (y, x) not in seen:
                    # Check l, r, u, d
                    if y+1 < Y and grid[y+1][x] == 1: 
                        grid[y+1][x] = 2
                        queue.append((y+1, x))

                    if x+1 < X and grid[y][x+1] == 1:
                        grid[y][x+1] = 2
                        queue.append((y, x+1))

                    if x-1 >= 0 and grid[y][x-1] == 1: 
                        grid[y][x-1] = 2
                        queue.append((y, x-1))

                    if y-1 >= 0 and grid[y-1][x] == 1:
                        grid[y-1][x] = 2
                        queue.append((y-1, x))
                    
                    seen.add((y, x))
            
            if len(fruits) > 0:
                total += 1
        
        if len(fruits) > 0:
            return -1
        return total
