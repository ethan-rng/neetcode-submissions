class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            # Open Bracket
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
                continue

            # Close Bracket
            if not stack:
                return False

            if bracket == ")" and stack[-1] == "(":
                stack.pop()
            elif bracket == "]" and stack[-1] == "[":
                stack.pop()
            elif bracket == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
            

        return len(stack) == 0