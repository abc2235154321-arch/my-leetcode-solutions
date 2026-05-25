from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        zero_count=0
        ans=0
        k=1
        for i in range(len(nums)):
            if nums[i]==0:
                zero_count+=1
            while(zero_count>k):
                if nums[left]==0:
                    zero_count-=1
                left+=1 
            ans=max(ans,i-left+1)       
        return ans-1
