class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        total = sum(nums)
        prefix = 0
        i = 0
        n = len(nums)
        while i<len(nums):
            if prefix == total - prefix - nums[i]:
                return i
            prefix += nums[i]
            i+=1
        return -1
        