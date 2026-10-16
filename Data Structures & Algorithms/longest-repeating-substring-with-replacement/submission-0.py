class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = defaultdict(int)
        l = 0
        output = 0

        def findMaxChar(maxChar):
            for char, freq in frequencies.items():
                if freq > frequencies[maxChar]:
                    maxChar = char
            
            return maxChar

        for r, currChar in enumerate(s):
            frequencies[currChar] += 1

            # Finding Max Out of Frequencies
            maxChar = findMaxChar(currChar)
           
            # Sliding Window
            while (r - l + 1) - (frequencies[maxChar]) > k:
                frequencies[s[l]] -= 1
                l += 1
                maxChar = findMaxChar(currChar)

            # Calculating Max Value
            output = max(output, r-l+1)

        return output




