class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return '/'
        elif strs[0] == '/':
            output += '/'
        else:
            output = ''

        for i, string in enumerate(strs):
            if i == len(strs) - 1:
                output += string
            else:
                output += string + "/"

        return output

    def decode(self, s: str) -> List[str]:
        if s == '/': return []

        word = ""
        output = []
        isReal = True

        for i, char in enumerate(s):
            if char == "/" and i+1 < len(s) and s[i+1] == "/":
                isReal = False
            elif not isReal and char == "/" and i+1 < len(s) and s[i+1] != "/":
                word.append("/")
                isReal = True
            elif char == "/" and isReal:
                output.append(word)
                word = ""
            else:
                word += char

        output.append(word)
        return output