class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split()
        p_to_w={}
        w_to_p={}
        if len(pattern) != len(word):
            return False

        for i,j in zip(pattern,word):
            if i in p_to_w:
                if p_to_w[i]!=j:
                    return False
            else:   
                p_to_w[i]=j
            if j in w_to_p:
                if w_to_p[j]!=i:
                    return False
            else:   
                w_to_p[j]=i
        return True