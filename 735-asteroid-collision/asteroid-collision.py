from typing import List
import math
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        steak=[]
        for i in range(len(asteroids)):
            alive=True
            while(steak and steak[-1]>0 and asteroids[i]<0):
                if steak[-1]<abs(asteroids[i]):
                    steak.pop()
                elif steak[-1]>abs(asteroids[i]): 
                    alive=False
                    break
                else:
                    steak.pop()
                    alive=False
                    break
            if alive:
                steak.append(asteroids[i])
        return steak 