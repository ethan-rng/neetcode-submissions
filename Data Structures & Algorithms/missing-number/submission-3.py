class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalCount, numsCount = 0, 0

        for i in range(0, len(nums)):
            totalCount += i
            numsCount += nums[i]

        totalCount += len(nums)
        return totalCount - numsCount 