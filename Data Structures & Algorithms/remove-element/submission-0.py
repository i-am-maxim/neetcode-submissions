class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = 0
        n = len(nums)

        while right<n:
            if nums[right] == val:
                nums.append(val)
            else:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left
        