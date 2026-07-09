from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count={}
        for i in words:
            count[i]=count.get(i,0)+1
        ans=[]
        items=sorted(count.items(),key=lambda x:(-x[1],x[0]))
        for i in range(k):
            ans.append(items[i][0])
        return ans