class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
        hashMap = {}
        maxCount=0
        left,right = 0, 0
        while(right<len(str) and left<len(str)):
            if str[right] not in hashMap:
                hashMap[str[right]] = 1
            else:
                while str[right] in hashMap:
                    del hashMap[str[left]]
                    left += 1
                hashMap[str[right]]=1
            maxCount = max(maxCount,hashMap.__len__())
            right+=1
        return max(maxCount,hashMap.__len__())

        