class Solution:
    def isValid(self, s: str) -> bool:
        check={"(":")","{":"}","[":"]"}
        steak=[]
        for i in s:
            if i in check:
                steak.append(i)
            else:
                if not steak:
                    return False
                a=steak.pop()
                if check[a]!=i:
                    return False
        return not steak
