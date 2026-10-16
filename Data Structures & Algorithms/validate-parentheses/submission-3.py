class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBrackets = "({["
        closeBrackets = ")]}"

        for char in s:
            print(char, stack)

            if char in openBrackets:
                stack.append(char)

            elif char in closeBrackets:
                if len(stack) == 0: return False

                topItem = stack[-1]
                
                if char == ")" and topItem == "(":
                    stack.pop()
                    continue
                elif char == ")":
                    return False
                
                if char == "}" and topItem == "{":
                    stack.pop()
                    continue
                elif char == "}":
                    return False
                
                if char == "]" and topItem == "[":
                    stack.pop()
                    continue
                elif char == "]":
                    return False

        print(stack, "jiiiii")
        return len(stack) == 0

        