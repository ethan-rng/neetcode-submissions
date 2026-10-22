class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        monotonic_stack = []

        for i, temp in enumerate(temperatures):
            if not monotonic_stack:
                monotonic_stack.append((i, temp))
                continue

            while monotonic_stack and temp > monotonic_stack[-1][1]:
                j, topTemp = monotonic_stack[-1]
                res[j] = i - j
                
                monotonic_stack.pop()

            # Add the curr temp
            monotonic_stack.append((i, temp))

        return res


        