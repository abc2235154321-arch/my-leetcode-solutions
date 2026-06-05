from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        queue=deque()
        fresh=0
        minutes=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append((r,c,0))

        if fresh==0:return 0
        directions=[(-1,0),(1,0),(0,-1),(0,1)]

        while queue:
            r,c,mins=queue.popleft()
            minutes=mins

            for dr ,dc in directions:
                nr,nc=dr+r,dc+c

                if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                    fresh-=1
                    grid[nr][nc]=2
                    queue.append((nr,nc,mins+1))
        return minutes if fresh==0 else -1
