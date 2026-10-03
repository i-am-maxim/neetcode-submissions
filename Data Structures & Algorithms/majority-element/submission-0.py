class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        currmax = 0
        ans = None
        for n in nums:
            count[n]+=1
            if count[n]>currmax:
                currmax = count[n]
                ans = n
        return ans