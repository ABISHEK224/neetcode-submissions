class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        need = {}
        left,right = 0,0
        current = 0
        for i in s1:
            need[i] = need.get(i,0)+1
        for right in range(len(s2)):
            current = s2[right]
            window[current] = window.get(current,0) + 1
            
            if right-left+1 > len(s1):
                leftchar = s2[left]
                window[leftchar] = window[leftchar] -1 
                
                if window[leftchar]==0:
                    del window[leftchar]
                left+=1
            if window == need:
                return True
                
        return False
            
            
                







            
        