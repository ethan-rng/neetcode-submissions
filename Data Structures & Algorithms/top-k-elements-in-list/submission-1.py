class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        reverseFreq = [deque() for _ in range(len(nums) + 1)]
        
        print(freqs)
        for freq in freqs:
            v = freqs[freq]
            print(v, freq)
            reverseFreq[v].append(freq)


        res = []
        print(reverseFreq)
        for i in range(len(nums), 0, -1):
            numFreq = reverseFreq[i]
            
            while numFreq and len(res) < k:
                num = numFreq.pop()
                res.append(num)
            
            if len(res) >= k:
                return res
            
        return res


