from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a=len(s)-1
        for i in range(len(s)//2):
            s[a] ,s[i]=s[i],s[a]
            a-=1
        