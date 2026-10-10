class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        prefixsum = 0
        for i,v in enumerate(nums):
            prefixsum += v
            nums[i] = prefixsum
        i = 0
        n = len(nums)
        while i<len(nums):
            if i==0 and nums[n-1]-nums[i]==0:
                return 0
            if nums[i-1] == nums[n-1]-nums[i]:
                return i
            else: i+=1
        return -1
        