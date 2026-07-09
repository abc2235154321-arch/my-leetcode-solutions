class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i not in count:
                count[i]=0
            count[i]+=1
        sort_count=sorted(count.items(),key=lambda x:x[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(sort_count[i][0])
        return ans