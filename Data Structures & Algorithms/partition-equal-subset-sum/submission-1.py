class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        if sumNums % 2 == 1: return False
        target = int(sumNums // 2)

        memo = defaultdict(bool)

        def dfs(n: int, numIndex: int, currTarget: int) -> bool:
            print(memo)
            key = (numIndex, currTarget)

            # Base Case 
            if currTarget == 0:
                return True

            # Base Case
            if numIndex >= len(nums):
                print("BYEE")
                return False
            
            if currTarget < 0:
                print("HII")
                return False
                
            # Memo
            if memo[key] in memo:
                return True
            
            num = nums[numIndex]
            memo[key] = dfs(n + 1, numIndex + 1, currTarget - num) \
                or dfs(n, numIndex + 1, currTarget)
            return memo[key]
        
        return dfs(0, 0, target)
