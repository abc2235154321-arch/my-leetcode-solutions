from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=0
        for fast in range(len(nums)):
            if nums[fast]!=val:
                nums[a]=nums[fast]
                a+=1
        return a