class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxLength = 0

        for i, num in enumerate(nums):
            # not beginning of the seq
            if num - 1 in nums_set: continue

            currLength = 1
            for offset in range(1, len(nums)):
                if num + offset not in nums_set: break

                currLength += 1

            maxLength = max(currLength, maxLength)


        return maxLength