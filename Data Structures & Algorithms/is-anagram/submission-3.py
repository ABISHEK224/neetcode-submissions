class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap={};
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        for i in t:
            if i not in hashMap or hashMap[i] <=0 :
                return False
            else:
                if i in hashMap and hashMap[i] >= 1:
                    hashMap[i]-=1

        return True