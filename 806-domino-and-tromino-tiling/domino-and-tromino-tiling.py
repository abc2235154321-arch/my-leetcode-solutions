class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        if n == 1: return 1

        flat = [0] * (n + 1)
        top = [0] * (n + 1)
        bottom = [0] * (n + 1)
        
        flat[0] = 1    
        flat[1] = 1   
        top[0] = 0
        top[1] = 0     
        bottom[0] = 0
        bottom[1] = 0  
        for i in range(2, n + 1):

            flat[i] = (flat[i-1] + flat[i-2] + top[i-1] + bottom[i-1]) % MOD
            

            top[i] = (flat[i-2] + bottom[i-1]) % MOD
            
            bottom[i] = (flat[i-2] + top[i-1]) % MOD
            
        return flat[n]