import math
from bisect import bisect_left
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        potions_length = len(potions)
        ans = []
        
        for i in spells:
            
            min_potion_needed = math.ceil(success / i)
            
            
            idx = bisect_left(potions, min_potion_needed)
            
            
            temp = potions_length - idx
            ans.append(temp)
            
        return ans