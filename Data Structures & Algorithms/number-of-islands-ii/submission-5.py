class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.rank = [0] * n
        self.parent = [-1] * n
        self.count = 0

    def find(self, a: int) -> int:
        if self.parent[a] == -1:
            raise ValueError("set isn't initialized")
        
        if self.parent[a] == a:
            return a

        # Path compression
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a: int, b: int) -> int:
        aRoot = self.find(a)
        bRoot = self.find(b)
        aRank = self.rank[aRoot]
        bRank = self.rank[bRoot]

        if aRoot == bRoot: return aRoot

        # Rank of Union
        newRoot = None
        if aRank < bRank:
            self.parent[aRoot] = bRoot
            newRoot = bRoot

        elif bRank < aRank:
            self.parent[bRoot] = aRoot
            newRoot = aRoot

        else:
            self.rank[a] += 1
            self.parent[bRoot] = aRoot
            newRoot = aRoot

        self.count -= 1
        return newRoot

    def add(self, a: int) -> int:
        if self.parent[a] != -1:
            return a
            
        self.parent[a] = a
        self.rank[a] += 1
        self.count += 1
        return a

    def isLand(self, a: int) -> bool:
        return self.parent[a] != -1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        Y, X = m, n
        unionFind = UnionFind(Y * X)
        res = []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for position in positions:
            y, x = position
            idx = y * X + x
            unionFind.add(idx)

            for yOffset, xOffset in dirs:
                idxX = x + xOffset
                idxY = y + yOffset

                if not(idxX < X and idxY < Y and idxX >= 0 and idxY >= 0):
                    continue

                newIdx = idxY * X + idxX
                if not unionFind.isLand(newIdx):
                    continue

                unionFind.union(idx, newIdx)

            res.append(unionFind.count)

        return res