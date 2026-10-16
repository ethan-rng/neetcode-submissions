class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        assert(len(equations) == len(values))
        orderedSet = defaultdict(int)
        neighbours = defaultdict(set)

        for i, equation in enumerate(equations):
            operand1, operand2 = equation
            value = values[i]

            orderedSet[(operand1, operand2)] = value
            orderedSet[(operand2, operand1)] = 1/value
            neighbours[operand1].add(operand2)
            neighbours[operand2].add(operand1)

        def dfs(operand, target):
            if operand not in neighbours:
                return -1
            if operand == target:
                return 1

            for neighbour in neighbours[operand]:
                if neighbour in visited:
                    continue

                visited.add(neighbour)
                res = dfs(neighbour, target)
                if res != -1:
                    return orderedSet[(operand, neighbour)] * res

            return -1

        results = []
        for query in queries:
            operand1, operand2 = query
            visited = set(operand1)

            res = dfs(operand1, operand2)
            results.append(res)
            """
                a / b = 10
                b / c = 5

                a / c = ? = 10 * 5 = 50

                a / b = 10
                c / b = 5
                a / c = ? = 10 / 5 = 2
            """
        return results

        