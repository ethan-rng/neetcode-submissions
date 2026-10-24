class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and len(edges) == 0: return True

        # Build Graph
        adjGraph = defaultdict(set)
        for edge in edges:
            src, dst = edge
            adjGraph[src].add(dst)
            adjGraph[dst].add(src)

        # Check if it is fully connected
        visited = set([0])
        step = 0
        def dfs(node: int) -> bool:
            nonlocal step
            if step == n:
                return len(visited) == n

            res = False
            for neighbor in adjGraph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    step += 1
                    dfs(neighbor)
            
            return len(visited) == n

        # check if hte number of edges is n -1
        return dfs(0) and len(edges) == n - 1