class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # table = [[0 for j in range(target+1)] for i in range(len(nums)+1)]
        memo = {}

        def _helper(numIndex: int, targetAdded: int) -> int:
            # Base Cases
            if targetAdded == target and numIndex == len(nums):
                return 1
            
            if numIndex == len(nums):
                return 0

            # Memo Result
            if (numIndex, targetAdded) in memo:
                return memo[(numIndex, targetAdded)]

            num = nums[numIndex]
            res = _helper(numIndex + 1, targetAdded - num) + \
                _helper(numIndex + 1, targetAdded + num)
            memo[(numIndex, targetAdded)] = res
            return res
        
        return _helper(0, 0)