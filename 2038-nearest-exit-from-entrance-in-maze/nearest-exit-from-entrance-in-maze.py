from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        start_row, start_col = entrance
        
        # 1. 準備 queue，裡面存 (當前橫列, 當前直行, 當前走過步數)
        queue = deque([(start_row, start_col, 0)])
        
        # 2. 把起點改為 '+'（原地蓋牆壁），防止之後走回頭路，省下一個 visited 集合的空間
        maze[start_row][start_col] = '+'
        
        # 定義四個方向：上、下、左、右
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, steps = queue.popleft()
            
            # 往四個方向探索
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # 檢查新位置是否在迷宮合法範圍內，且是空地 '.'
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                    
                    # 💡 關鍵判斷：這個空地是否位於邊界？（如果是，它就是出口！）
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return steps + 1 # 第一次踩到邊界，絕對是最短步數！
                    
                    # 如果不是出口，標記為已造訪（蓋牆壁），並丟進 queue 繼續前進
                    maze[nr][nc] = '+'
                    queue.append((nr, nc, steps + 1))
                    
        return -1 # 走遍了都找不到出口