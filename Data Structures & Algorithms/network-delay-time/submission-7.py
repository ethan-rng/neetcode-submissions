class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # O(V+E)log(V)

        graph = defaultdict(set)
        distances = {i: 0 if i == k else float('inf') for i in range(1, n+1)}
        heap = [(0, k) if _ == k else (float('inf'), k) for _ in range(1, n+1)]
        heapq.heapify(heap)

        # build graph
        for time in times:
            source, dst, w = time
            graph[source].add((dst, w))

        while heap:
            totalW, node = heapq.heappop(heap)  
        
            if totalW > distances[node]:
                continue
            
            # Update Heap via all neighbours
            for neighbor in graph[node]:
                dst, w = neighbor

                if distances[dst] > totalW + w:
                    heapq.heappush(heap, (totalW + w, dst))
                    distances[dst] = min(distances[dst], totalW + w)
        
        res = max(distances[node] for node in distances)
        return -1 if res == float('inf') else res