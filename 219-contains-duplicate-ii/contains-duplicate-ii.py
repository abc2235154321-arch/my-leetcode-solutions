from typing import List 
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dist={}
        for i ,j in enumerate(nums):
            if j in dist and i-dist[j]<=k:
                return True
            dist[j]=i
        return False