class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points: return 0

        n = len(points)
        matrix = defaultdict(set)

        # Generate All Points n * n
        for src in points:
            for dst in points:
                src = (src[0], src[1])
                dst = (dst[0], dst[1])

                if src == dst: continue

                W = abs(src[0] - dst[0]) + abs(src[1] - dst[1])
                srcW = (W, src[0], src[1])
                dstW = (W, dst[0], dst[1])

                matrix[src].add(dstW)
                matrix[dst].add(srcW)

        # Using Prim-Jarnick
        edges = list(matrix[tuple(points[0])])
        heapq.heapify(edges)
        seenNodes = set([(points[0][0], points[0][1])]) # add node zero
        total = 0

        while len(seenNodes) < n:        
            edgeTuple = heapq.heappop(edges)
            W, x, y = edgeTuple

            if (x, y) in seenNodes: continue
            seenNodes.add((x, y))
            total += W

            # Add new edges
            for neighbour in matrix[(x, y)]:
                _, dstX, dstY = neighbour

                if (dstX, dstY) in seenNodes: continue
                heapq.heappush(edges, neighbour)

        print(seenNodes)
        return total


        