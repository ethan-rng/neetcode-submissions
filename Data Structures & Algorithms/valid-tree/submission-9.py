class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)

        for edge in edges:
            graph[edge[1]].add(edge[0])
            graph[edge[0]].add(edge[1])
        
        print(graph)
        # RUN A DFS SEARCH ON ANY NODE, IF WE VISITED AGAIN WE R COOKED
        visited = set()

        def dfs(node, prev):
            if not graph[node]:
                return True
            # cycle detected
            if node != prev and node in visited:
                return False

            visited.add(node)
            for neighbour in graph[node]:
                if neighbour != prev and not dfs(neighbour, node):
                    return False

            return True

        for node in graph:
            output = dfs(node, None)
            break
        
        if n == 1 and len(graph.keys()) == 0:
            return True
        if len(visited) == n and n != 1:
            return output
        return False