from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        while right>left:
            mid=(right+left)//2
            cost=0
            for i in piles:
                cost+=math.ceil(i/mid)
            if cost >h:
                left=mid+1
            else:
                right=mid
        return left
