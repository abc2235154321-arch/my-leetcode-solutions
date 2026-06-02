from typing import List
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited={0}
        queue=deque([0])
        while queue:
            curr=queue.popleft()
            for i in rooms[curr]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        return len(visited)==len(rooms)