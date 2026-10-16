class Solution:
    def checkInclusion(self, s2: str, s1: str) -> bool:
        if len(s1) < len(s2):
            print("HI")
            return False

        l, r = 0, len(s2) - 1
        freq = Counter(s2)
        currFreq = defaultdict(int)
        
        for i in range(len(s2)):
            currFreq[s1[i]] += 1
        print(currFreq)
        print(len(s1))
        print(s1, s2)


        while r < len(s1):
            # check if currFreq = freq
            isMatch = True
            for key in freq.keys():
                if currFreq[key] != freq[key]:
                    isMatch = False
                    break
            if isMatch: 
                print(currFreq, freq, l, r)
                return True

            currFreq[s1[l]] -= 1
            l += 1
            r += 1
            if r >= len(s1): break
            currFreq[s1[r]] += 1
        return False    
         

       

        