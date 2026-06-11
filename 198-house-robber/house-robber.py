from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[]
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            if i==0 or i==1:
                dp.append(nums[i])
            else:
                dp.append(max(dp[:-1])+nums[i])
        return max(dp)