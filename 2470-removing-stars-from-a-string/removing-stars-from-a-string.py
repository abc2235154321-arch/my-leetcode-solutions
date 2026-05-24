class Solution:
    def removeStars(self, s: str) -> str:
        steak=[]
        for i in s:
            if i=="*":
                steak.pop()
            else:
                steak.append(i)
        return "".join(steak)