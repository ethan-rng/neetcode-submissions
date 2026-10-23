"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        valToNode = defaultdict(Node)
        visited = set()

        def dfs(ogRoot: Optional['Node']) -> Optional['Node']:
            if not ogRoot: return None
            val = ogRoot.val

            # Node Creation Process
            if val in valToNode:
                newRoot = valToNode[val]
            else:
                newRoot = Node(val)
                valToNode[val] = newRoot
            
            # Creating Neighbors
            for ogNeighbor in ogRoot.neighbors:
                # if ogNeighbor.val in visited: continue

                if ogNeighbor.val in valToNode:
                    newRoot.neighbors.append(valToNode[ogNeighbor.val])
                    continue
                
                newRoot.neighbors.append(dfs(ogNeighbor))
                visited.add(ogNeighbor.val)

            return newRoot
        
        return dfs(node)
        