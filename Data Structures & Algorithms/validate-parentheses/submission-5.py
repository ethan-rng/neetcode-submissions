class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        conversions = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for bracket in s:
            # Open Bracket
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
                continue

            # Close Bracket
            if not stack:
                return False

            if bracket not in conversions.keys():
                return False

            if conversions[bracket] != stack[-1]:
                return False
           
            stack.pop()

        return len(stack) == 0