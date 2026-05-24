from collections import Counter
from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        ans=0
        row_count=Counter()
        for i in grid:
            row_tuple=tuple(i)
            row_count[row_tuple]+=1
        for i in range(n):
            col_list =[]
            for j in range(n):
                col_list.append(grid[j][i])
            col_tuple = tuple(col_list)
            ans+=row_count[col_tuple]
        return ans