from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        length=len(senate)
        r=deque()
        d=deque()
        for i,j in enumerate(senate):
            if j=='R':
                r.append(i)
            else:
                d.append(i)
        while(r and d):
            if r[0] <d[0]:
                r.append(r[0]+length)
                r.popleft()
                d.popleft()
            else:
                d.append(d[0]+length)                
                d.popleft()
                r.popleft()
        if not r:
            return 'Dire'
        else: 
            return 'Radiant'