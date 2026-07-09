class Solution:
    def frequencySort(self, s: str) -> str:
        count={}
        for i in s:
            if i not in count:
                count[i]=0
            count[i]+=1
        ans=sorted(count.items(),key=lambda x:x[1],reverse=True)
        a=''
        for i,j in ans:
           a+=i*j
        return a 