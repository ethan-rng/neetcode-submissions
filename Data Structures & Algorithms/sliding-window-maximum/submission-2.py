class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque([])
        res = []
        n = len(nums)
             
        # Before Fill
        for i, num in enumerate(nums[:k]):
            # Pop off parts that are not needed
            while window and window[-1][1] < num:
                window.pop()
            
            window.append((i, num))        

        for idx, num in enumerate(nums[k:]):
            i = idx + k
            # print(i-k, i-1, window)
            
            res.append(window[0][1])
            # Remove out of bounds part
            while window and window[0][0] <= i-k:
                # print(i-1, "AA")
                window.popleft()
            
            # Pop off parts that are not needed
            while window and window[-1][1] < num:
                # print(i-1, "BB")
                window.pop()
            
            window.append((i, num))
        
        # print(n-1, window)
        res.append(window[0][1])
        return res