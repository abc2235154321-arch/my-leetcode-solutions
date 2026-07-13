class Solution:
    def longestPalindrome(self, s: str) -> int:
        count={}
        ans=0
        odd=False
        for i in s:
            if i not in count:
                count[i]=0
            count[i]+=1
        for i in count.values():
            if i%2==0:
                ans+=i
            else:
                ans+=i-1
                odd=True
        if odd:
            ans+=1
        return ans
        