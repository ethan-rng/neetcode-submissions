class Solution:
    def minRemoveToMakeValid(self, string: str) -> str:
        stack = deque([])

        for i, s in enumerate(string):
            # open bracket case
            if s == "(":
                stack.append((i, "("))
                continue

            # close bracket cases
            if stack and stack[-1][1] == "(" and s == ')':
                stack.pop()
                continue
            
            if s == ")":
                stack.append((i, ")"))
                continue
        
        # create new string
        res = ""
        for i, s in enumerate(string):
            if stack and stack[0][0] == i and s in {"(", ")"}:
                stack.popleft()
                continue
            
            res += s
        
        return res
                