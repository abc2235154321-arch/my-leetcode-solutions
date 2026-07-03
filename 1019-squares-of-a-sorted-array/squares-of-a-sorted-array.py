from typing import List
import math
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[(abs(i)**2)for i in nums]
        return sorted(a)